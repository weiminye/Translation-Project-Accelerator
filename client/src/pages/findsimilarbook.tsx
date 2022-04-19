import React from 'react';
import { useEffect } from 'react';

import { PageContainer } from '@ant-design/pro-layout';
import { Row, Col, Form, Input, Button, Table, message, Typography } from 'antd';
import { useIntl, FormattedMessage } from 'umi';
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
    <PageContainer loading={loading}>
      <Row gutter={46}>
        {
          !(data) && <Col span={12}><Form
            name="basic"
            onFinish={async (values) => {
              await handleSubmit(values);
            }}
            autoComplete="off"
          >
            <Form.Item
              label="Name of the book"
              name="bookname"
              rules={[{ required: true, message: 'Please input name of the book!' }]}
            >
              <Input />
            </Form.Item>
            <Form.Item
              label="Table of contents"
              name="tableofcontents"
              rules={[{ required: true, message: 'Please input Table of contents!' }]}
            >
              <TextArea rows={14} />
            </Form.Item>
            <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
              <Button type="primary" htmlType="submit">
                Submit
              </Button>
            </Form.Item>
          </Form></Col>
        }
        {
          data &&
          <Col span={24}>
            {
              data &&
              <>
                <Title  level={2}>Your Book:
                  {data.bookname}</Title>
                  <Title  level={4}>Similar Books：</Title>
                <Table columns={columns} dataSource={data.result} loading={loading}/>
              </>
            }
          </Col>
        }
      </Row>
    </PageContainer >
  );
};

export default findsimilarbook;
