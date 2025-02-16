import { useState, useEffect } from "react";
import ollamaLogo from "./assets/ollama.svg";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState(["Waiting for a message..."]);
  const [question, setQuestion] = useState("Ask your question and enter here");

  const handleQuestion = async (e) => {
    e.preventDefault();
    setLoading(true);
    setQuestion("");
    try {
      const result = await fetch("http://localhost:8000/question", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });

      const data = await result.json();
      setMessage(data.message.split("\n\n"));
      console.log(message);
    } catch (error) {
      console.error(error);
      setLoading(false);
    } finally {
      setLoading(false);
    }
  };

  const handleFileChange = (e) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
      handleUpload();
    }
  };

  const handleUpload = async () => {
    if (file) {
      console.log("Uploading file...");

      const formData = new FormData();
      formData.append("file", file);

      try {
        const result = await fetch("http://localhost:8000/file", {
          method: "POST",
          body: formData,
        });

        const data = await result.json();

        console.log(data);
      } catch (error) {
        console.error(error);
      }
    }
  };

  useEffect(() => {
    if (file) {
      handleUpload(file);
    }
  }, [file]);

  return (
    <>
      <div>
        <img src={ollamaLogo} className="logo" />
      </div>
      <h1>Document Chat</h1>
      <div className="appContainer">
        <div className="chat">
          <div className="messages">
            {message.map((mess, index) => {
              return <div key={index}>{mess}</div>;
            })}
          </div>
          <form onSubmit={handleQuestion}>
            <input
              type="text"
              className="question"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
            ></input>
          </form>
          {loading && <div className="loading">Generating answer...</div>}
        </div>
      </div>
      <input type="file" accept=".pdf" id="file" onChange={handleFileChange} />
      {file && <div>Chatbot is using file: {file.name}</div>}
    </>
  );
}

export default App;
