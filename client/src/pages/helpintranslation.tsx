import React from 'react';
import { useEffect } from 'react';

import { PageContainer } from '@ant-design/pro-layout';
import { Tabs, Row, Col, Form, Input, Button, Table, message, Typography } from 'antd';
import { useRequest } from 'umi';
import { CheckCircleTwoTone } from '@ant-design/icons';

const { TabPane } = Tabs;
const findsimilarbook: React.FC = () => {
  const { Title } = Typography;
  // const data = [];
  const { data, run, loading } = useRequest((sentence) => ({
    url: '/api/find_similar_translation',
    method: 'post',
    data: { sentence },
  }), { manual: true })

  function callback(key) {
    console.log(key);
    try {
      // (data) = await findsimilarbookfromserver({ ...values });
      run(key)
    } catch (error) {
      message.error(error);
    }
  }

  const { TextArea } = Input;

  // const { data} = useRequest(backend_server_health_check);

  const columns = [
    {
      width: 150,
      title: 'Similarity',
      dataIndex: 'similarity',
      defaultSortOrder: 'descend',
      sorter: (a, b) => a.similarity - b.similarity,
    },
    {
      title: 'Sentence',
      dataIndex: 'sentence',
    },
    {
      title: 'Translation',
      dataIndex: 'translation',
    },
  ];

  useEffect(() => {
  }, data);

  return (
    <PageContainer>
      <Row>
        <Col span={24}>
          <Title level={4}>Book:
            C# 10 in a Nutshell</Title>
        </Col>
      </Row>
      <Row>
        <Col span={6}>
          <Tabs tabPosition="left" type="card" onChange={callback}>
            <TabPane tab={<span>
              <CheckCircleTwoTone twoToneColor="#52c41a" />
              What’s New in C# 10
            </span>} key="What’s New in C# 10">
            </TabPane>
            <TabPane tab={<span>
              <CheckCircleTwoTone twoToneColor="#52c41a" />
              What’s New in C# 9.0
            </span>} key="What’s New in C# 9.0">
            </TabPane>
            <TabPane tab={<span>
              <CheckCircleTwoTone twoToneColor="#52c41a" />
              What’s New in C# 8.0
            </span>} key="What’s New in C# 8.0">
            </TabPane>
            <TabPane tab={<span>
              <CheckCircleTwoTone twoToneColor="#52c41a" />
              What’s New in C# 7.x
            </span>} key="What’s New in C# 7.x">
            </TabPane>
            <TabPane tab={<span>
              <CheckCircleTwoTone twoToneColor="#52c41a" />
              What’s New in C# 6.0
            </span>} key="What’s New in C# 6.0">
            </TabPane>
            <TabPane tab={<span>
              <CheckCircleTwoTone twoToneColor="#52c41a" />
              What’s New in C# 5.0
            </span>} key="What’s New in C# 5.0">
            </TabPane>
            <TabPane tab={<span>
              <CheckCircleTwoTone twoToneColor="#52c41a" />
              What’s New in C# 4.0
            </span>} key="What’s New in C# 4.0">
            </TabPane>
            <TabPane tab="What’s New in C# 3.0" key="What’s New in C# 3.0">
            </TabPane>
            <TabPane tab="What’s New in C# 2.0" key="What’s New in C# 2.0">
            </TabPane>
            <TabPane tab="2. C# Language Basics" key="2. C# Language Basics">
            </TabPane>
            <TabPane tab="A First C# Program" key="A First C# Program">
            </TabPane>
            <TabPane tab="Compilation" key="Compilation">
            </TabPane>
            <TabPane tab="Syntax" key="Syntax">
            </TabPane>
          </Tabs>
        </Col>
        {
          data &&
          <Col span={18}>
            <Form
              layout="inline"
              name="basic"
              onFinish={async (values) => {
                await handleSubmit(values);
              }}
              autoComplete="off"
            >
              <Form.Item
                label="Your Translation"
                name="translation"
                rules={[{ required: true, message: 'Please input your translation!' }]}
              >
                <Input style={{ width: '400px' }} />
              </Form.Item>
              <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
                <Button type="primary" htmlType="submit">
                  Submit
                </Button>
              </Form.Item>
            </Form>
            <Title level={4}>Translation of Similar Sentence:</Title>
            <Table columns={columns} dataSource={data} loading={loading}/>
          </Col>
        }
      </Row>
    </PageContainer >
  );
};

export default findsimilarbook;
