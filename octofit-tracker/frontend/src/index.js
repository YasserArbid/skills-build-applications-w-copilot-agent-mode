
import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';

// Make sure REACT_APP_CODESPACE_NAME is set in your environment for API calls
console.log('REACT_APP_CODESPACE_NAME:', process.env.REACT_APP_CODESPACE_NAME);

const root = createRoot(document.getElementById('root'));
root.render(
  <StrictMode>
    <App />
  </StrictMode>
);

reportWebVitals();
