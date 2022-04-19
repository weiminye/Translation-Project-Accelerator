server = 'https://billyinusa-test.i.tgcloud.io/'

data_folder = r'data'

import re

def remove_prefix(text):
    strinfo = re.compile('\d+. |\d+.\d+. |\d+.\d+.\d+. |\d+ |\d+.\d+ |\d+.\d+.\d+ ')
    result = strinfo.sub('', text)
    return result

import os
def list_all_data_files(folder):
    file_list = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower().endswith('.txt'):
                file_list.append(os.path.join(root, file))
    return file_list

data_file_list = list_all_data_files(data_folder)

import getpass
password = getpass.getpass()

import pyTigerGraph as tg 

conn = tg.TigerGraphConnection(host=server,graphname='Translation_Project_Management', password=password)

print(conn.gsql('''
USE GLOBAL

// Clear the current catalog.
DROP ALL

// Create vertex types.
CREATE VERTEX translator (PRIMARY_ID name string,name string)
CREATE VERTEX book (PRIMARY_ID name string,name string,translator string)
CREATE VERTEX sentence (PRIMARY_ID text string,text string,translation string)
CREATE VERTEX word (PRIMARY_ID lemma string,lemma string)

// Create edge types.
CREATE DIRECTED EDGE translated_by (FROM book, TO translator) WITH REVERSE_EDGE="reverse_translated_by"
CREATE DIRECTED EDGE has (FROM book, TO sentence) WITH REVERSE_EDGE="reverse_has"
CREATE DIRECTED EDGE contains (FROM sentence, TO word) WITH REVERSE_EDGE="reverse_contains"
CREATE DIRECTED EDGE next (FROM word, TO word) WITH REVERSE_EDGE="reverse_next"

create graph Translation_Project_Management (*)
    '''))

secret = conn.createSecret()
conn.getToken(secret=secret)

# 获取数据文件的文件名
def get_file_name(data_file_list):
    file_name_list = []
    for i in data_file_list:
        file_name_list.append(os.path.basename(i).replace('.txt',''))
    return file_name_list

file_name_list = get_file_name(data_file_list)

import pandas as pd

books = pd.DataFrame(file_name_list, columns=['name'])
books['translator'] = 'Jack'
books.loc[3,'translator'] = 'John'
books.loc[4,'translator'] = 'John'
books.loc[5,'translator'] = 'John'
books.loc[6,'translator'] = 'John'
books.loc[7,'translator'] = 'Tom'
books.loc[8,'translator'] = 'Tom'
books.loc[9,'translator'] = 'Tom'

conn.upsertVertexDataFrame(df=books, vertexType='book', v_id='name')

import spacy
nlp = spacy.load("en_core_web_sm")

def replace_special_char(text):
    return text.replace("C#","CSharp").replace(".NET","dotNET")

def generate_df_from_file(current_file_path):
    with open(current_file_path, 'r', encoding='utf-8') as f:
        sentence_text_list = f.readlines()
    
    sentence_text_list = [remove_prefix(replace_special_char(i.replace('\n', ''))) for i in sentence_text_list]
    return sentence_text_list

def split_sentence_to_word(sentence):    
    doc = nlp(sentence)
    lemma_list = [token.lemma_ for token in doc]
    words = pd.DataFrame(lemma_list, columns=['lemma'])
    words_belong_sentence = pd.DataFrame(lemma_list, columns=['word'])
    words_belong_sentence['sentence'] = sentence
    words_relationship_pd = pd.DataFrame()
    words_relationship_pd['from'] = words.shift(axis=0)['lemma']
    words_relationship_pd['to'] = words['lemma']
    words_relationship_pd = words_relationship_pd.dropna()
    return (words,words_belong_sentence,words_relationship_pd)

def import_sentence_into_database(sentence_list,file_name):
    sentence = pd.DataFrame(sentence_list, columns=['text'])
    sentence["book"] = file_name
    sentence_onlyVertex = sentence[['text']]

    translation_df = pd.read_csv('data/translation.csv', encoding='utf-8')
    sentence_onlyVertex = sentence_onlyVertex.merge(translation_df, left_on='text', right_on='sentence', how='left')

    sentence_onlyVertex['translation'] = sentence_onlyVertex['translation'].fillna('')

    sentence_onlyVertex = sentence_onlyVertex[['text','translation']]
    conn.upsertVertexDataFrame(df=sentence_onlyVertex, vertexType='sentence', v_id='text')

    conn.upsertEdgeDataFrame(df=sentence,sourceVertexType='book',edgeType='has',targetVertexType='sentence',from_id='book',to_id='text',attributes={})

    words_all = pd.DataFrame()
    words_belong_sentence_all = pd.DataFrame()
    words_relationship_pd_all = pd.DataFrame()
    for i in range(len(sentence_list)):               
        (words,words_belong_sentence,words_relationship_pd) = split_sentence_to_word(sentence_list[i])
        words_all = pd.concat([words_all,words.reset_index(drop=True)])
        words_belong_sentence_all = pd.concat([words_belong_sentence_all,words_belong_sentence.reset_index(drop=True)])
        words_relationship_pd_all = pd.concat([words_relationship_pd_all,words_relationship_pd.reset_index(drop=True)])

    words_all = words_all.reset_index()
    conn.upsertVertexDataFrame(df=words_all, vertexType='word', v_id='lemma',attributes={})
    words_belong_sentence_all = words_belong_sentence_all.reset_index()
    conn.upsertEdgeDataFrame(df=words_belong_sentence_all,sourceVertexType='sentence', edgeType='contains',targetVertexType='word', from_id='sentence', to_id='word',attributes={})
    words_relationship_pd_all = words_relationship_pd_all.reset_index()
    # disable the the below code for performance issue, will resolve it in future
    # conn.upsertEdgeDataFrame(df=words_relationship_pd_all,sourceVertexType='word', edgeType='next',targetVertexType='word', from_id='from', to_id='to',attributes={})
    # sentence.to_csv('debug\\'+文件名+'words_relationship_pd_all.csv', index=False, encoding='utf-8')
    
for i in data_file_list:
    current_file_name = os.path.basename(i).replace('.txt','')
    import_sentence_into_database(generate_df_from_file(i),current_file_name)