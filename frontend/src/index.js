// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';  // Import any global styles here (optional)
import './App.css';    // Import the App styles here if preferred
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
