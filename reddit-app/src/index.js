import React from 'react';
import ReactDOM from 'react-dom';
import { ChakraProvider } from '@chakra-ui/react';
import App from './App';
import Header from './components/Header'


ReactDOM.render(
  <ChakraProvider>
    <Header />
    <App />
  </ChakraProvider>,
  document.getElementById('root')
);
