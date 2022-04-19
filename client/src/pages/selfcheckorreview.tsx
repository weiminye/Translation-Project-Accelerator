import React from 'react';
import { useEffect } from 'react';

import { PageContainer } from '@ant-design/pro-layout';
import { Space, Row, Col, Form, Input, Button, Table, message, Typography } from 'antd';
import { useRequest } from 'umi';
import { findsimilarbookfromserver } from '@/services/ant-design-pro/api';

const findsimilarbook: React.FC = () => {
  const { Title, Paragraph, Text, Link } = Typography;
  // const data = [];
  const { data, run, loading } = useRequest(findsimilarbookfromserver, { manual: true })

  const handleSubmit = async (values) => {
    console.log('Success:', values);
    try {
      // (data) = await findsimilarbookfromserver({ ...values });
      run({ ...values })
    } catch (error) {
      message.error(error);
    }
  };

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
      title: 'Book Name',
      dataIndex: 'bookname',
    },
    {
      title: 'Translator',
      dataIndex: 'translator',
    },
  ];

  useEffect(() => {
  }, data);

  return (
    <PageContainer>
      <Form
        layout="inline"
        name="basic"
        onFinish={async (values) => {
          await handleSubmit(values);
        }}
        autoComplete="off"
      >
        <Row gutter={46}>
          <Col span={12}>
            <Title level={4}>Original Content: (Will support upload file in future)</Title>
            <TextArea rows={24} />
          </Col>

          <Col span={12}>
            <Title level={4}>Your Translation: (Will support upload file in future)</Title>
            <TextArea rows={24} />
          </Col>
        </Row>
        <Row gutter={46} justify="center" align="middle">
          <div>
            <p></p><p></p>
            <p></p><p></p>
            <Button type="primary">
              Submit to Self Check Or Review
            </Button>
            <p></p><p></p>
            <p></p><p></p>
          </div>
        </Row>
      </Form>
    </PageContainer >
  );
};

export default findsimilarbook;
