from flask import Flask, request, jsonify,Response
from joblib import dump, load
import random
from flask_cors import CORS
from enum import Enum

from icecream import ic
import time

import pandas as pd

import getpass

server = 'https://billyinusa-test.i.tgcloud.io/'
password = getpass.getpass()

import pyTigerGraph as tg 

conn = tg.TigerGraphConnection(host=server,graphname='Translation_Project_Management', password=password)

secret = conn.createSecret()
conn.getToken(secret=secret);

import json
import spacy
# nlp = spacy.load("en_core_web_trf")
nlp = spacy.load("en_core_web_sm")

import re

def remove_prefix(text):
    strinfo = re.compile('\d+. |\d+.\d+. |\d+.\d+.\d+. |\d+ |\d+.\d+ |\d+.\d+.\d+ ')    # 注意用4个\\\\来替换\
    result = strinfo.sub('', text)
    return result

def replace_special_char(text):
    return text.replace("C#","CSharp").replace(".NET","dotNET")

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

def find_similar_book_core(bookname,tableofcontents):
    bookname = bookname.strip()
    tableofcontents = tableofcontents.strip()
    sentence_list = tableofcontents.split("\n")
    sentence_list = [remove_prefix(replace_special_char(i.strip().replace('\n', ''))) for i in sentence_list]

    sentence = pd.DataFrame(sentence_list, columns=['text'])
    sentence["book"] = bookname
    sentence_onlyVertex = sentence[['text']]
    conn.upsertVertexDataFrame(df=sentence_onlyVertex, vertexType='sentence', v_id='text')

    conn.upsertEdgeDataFrame(df=sentence,sourceVertexType='book',edgeType='has',targetVertexType='sentence',from_id='book',to_id='text',attributes={})

    words_all = pd.DataFrame()
    words_belong_sentence_all = pd.DataFrame()
    words_relationship_pd_all = pd.DataFrame()
    # 遍历sentence_list，将每个sentence的单词导入到数据库中
    for i in range(len(sentence_list)):               
        (words,words_belong_sentence,words_relationship_pd) = split_sentence_to_word(sentence_list[i])
        words_all = pd.concat([words_all,words.reset_index(drop=True)])
        words_belong_sentence_all = pd.concat([words_belong_sentence_all,words_belong_sentence.reset_index(drop=True)])
        words_relationship_pd_all = pd.concat([words_relationship_pd_all,words_relationship_pd.reset_index(drop=True)])

    words_all = words_all.reset_index()
    # ic(words_all)
    conn.upsertVertexDataFrame(df=words_all, vertexType='word', v_id='lemma',attributes={})
    words_belong_sentence_all = words_belong_sentence_all.reset_index()
    conn.upsertEdgeDataFrame(df=words_belong_sentence_all,sourceVertexType='sentence', edgeType='contains',targetVertexType='word', from_id='sentence', to_id='word',attributes={})

    # disable the the below code for performance issue, will resolve it in future
    # words_relationship_pd_all = words_relationship_pd_all.reset_index()
    # conn.upsertEdgeDataFrame(df=words_relationship_pd_all,sourceVertexType='word', edgeType='next',targetVertexType='word', from_id='from', to_id='to',attributes={})

    json_result = conn.runInstalledQuery('tg_jaccard_nbor_ss',{"source": bookname,"source.type":"book","e_type":"has","rev_e_type":"reverse_has","top_k":500})

    return json_result

def find_similar_translation_core(sentence):
    sentence = remove_prefix(replace_special_char(sentence.strip().replace('\n', '')))

    sentence_df = pd.DataFrame([sentence], columns=['text'])
    sentence_onlyVertex_df = sentence_df[['text']]
    conn.upsertVertexDataFrame(df=sentence_onlyVertex_df, vertexType='sentence', v_id='text')
    
    (words,words_belong_sentence,words_relationship_pd) = split_sentence_to_word(sentence)

    conn.upsertVertexDataFrame(df=words, vertexType='word', v_id='lemma',attributes={})
    conn.upsertEdgeDataFrame(df=words_belong_sentence,sourceVertexType='sentence', edgeType='contains',targetVertexType='word', from_id='sentence', to_id='word',attributes={})

    # disable the the below code for performance issue, will resolve it in future
    # words_relationship_pd_all = words_relationship_pd_all.reset_index()
    # conn.upsertEdgeDataFrame(df=words_relationship_pd_all,sourceVertexType='word', edgeType='next',targetVertexType='word', from_id='from', to_id='to',attributes={})

    json_result = conn.runInstalledQuery('tg_jaccard_nbor_ss',{"source": sentence,"source.type":"sentence","e_type":"contains","rev_e_type":"reverse_contains","top_k":5})

    return json_result

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/")
def helloWorld():
    return "Hello World!"

@app.route("/api/health_check")
def health_check():
    # time.sleep(5) # use to test frontend welcome page loading
    return { 'data': {'status': 'success','message':'Backend server works fine!','description':''}}

@app.route('/api/find_similar_book', methods=['POST'])
def find_similar_book():
    data = request.json
    bookname = data['bookname']
    tableofcontents = data['tableofcontents']
    result_from_db = find_similar_book_core(bookname,tableofcontents)
    final_return_result =  []
    useful_data = result_from_db[0]["Others"]
    for current in useful_data:        
        final_return_result.append({'bookname':current['v_id'],'translator':current['attributes']['translator'],'similarity':current['attributes']['@sum_similarity']})
    return jsonify({ 'data':{'bookname':bookname,'tableofcontents':tableofcontents,'result':final_return_result}})    

@app.route('/api/find_similar_translation', methods=['POST'])
def find_similar_translation():
    data = request.json
    sentence = data['sentence']
    result_from_db = find_similar_translation_core(sentence)
    final_return_result =  []
    useful_data = result_from_db[0]["Others"]
    for current in useful_data:        
        final_return_result.append({'sentence':current['v_id'],'translation':current['attributes']['translation'],'similarity':current['attributes']['@sum_similarity']})
    return jsonify({ 'data':final_return_result})

app.run()
