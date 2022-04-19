import React from 'react';
import { useEffect } from 'react';

import { PageContainer } from '@ant-design/pro-layout';
import { Card, Alert, Typography } from 'antd';
import { useIntl, FormattedMessage } from 'umi';
import styles from './Welcome.less';
import { useRequest } from 'umi';
import { backend_server_health_check } from '@/services/ant-design-pro/api';

const Welcome: React.FC = () => {
  const  {loading, data, error, params, cancel, refresh, mutate, run, unmount, fetches, reset} = useRequest(backend_server_health_check);

  useEffect(() => {    
    document.title = data ? data.message : "Can't connect to server";
  }, data);

  // if (error) return <PageContainer><div>failed to load</div></PageContainer>
  if (loading) return <PageContainer><div>loading...</div></PageContainer>
  
  return (
    <PageContainer>
      <Alert
        message={data ? data.message : "Can't connect to server"}
        description={data ? data.description : "Please start backend server and make sure there is correct config at your proxy.ts."}
        type={data ? data.status : 'error'}
        showIcon
      />
    </PageContainer>
  );
};

export default Welcome;
