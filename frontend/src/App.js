// src/App.js
import React, { useState } from 'react';
import { processReceipt } from './api';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [output, setOutput] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false); // Loading state for the spinner

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setOutput(null);
    setError(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      alert("Please upload an image.");
      return;
    }

    setLoading(true);
    setError(null);
    setOutput(null);

    try {
      const response = await processReceipt(file);
      setOutput(response.data);
    } catch (err) {
      console.error("Error processing file:", err);
      setError("There was an error processing the file. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Receipt Reader</h1>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="image/*" onChange={handleFileChange} />
        <button type="submit">Upload and Process</button>
      </form>

      {/* Display loading spinner */}
      {loading && <div className="loader"></div>}

      {/* Display error message */}
      {error && <div className="error-message">{error}</div>}

      {/* Display JSON output */}
      {output && (
        <div>
          <h2>Processed Receipt Data:</h2>
          <pre>{JSON.stringify(output, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
