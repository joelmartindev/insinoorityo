import { useState } from "react";
import "./App.css";

const App = () => {
  const [text, setText] = useState(null);
  const [translations, setTranslations] = useState([]);

  const sendRequest = async () => {
    const response = await fetch("http://localhost:5000/translate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });

    let data = await response.json();
    data = data.translation;
    return data;
  };

  const translate = async () => {
    const newTranslation = await sendRequest(text);
    setTranslations([...translations, newTranslation]);
  };

  return (
    <>
      <h2>EN to FI Translator</h2>
      <div className="translations">
        {translations.map((item, index) => (
          <div key={index}>
            <h3>{"Translation #" + (index + 1)}</h3>
            <p>{item}</p>
          </div>
        ))}
      </div>
      <textarea
        placeholder="Text to translate"
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={translate}>Translate</button>
    </>
  );
};

export default App;
