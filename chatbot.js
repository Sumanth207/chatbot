import React, { useState } from "react";
import axios from "axios";

const Chatbot = () => {
    const [input, setInput] = useState("");
    const [messages, setMessages] = useState([]);

    const sendMessage = async () => {
        if (!input.trim()) return;
        const response = await axios.post("http://127.0.0.1:8000/chat", { user_input: input });
        setMessages([...messages, { user: input, bot: response.data.response }]);
        setInput("");
    };

    return (
        <div>
            <div className="chat-container">
                {messages.map((msg, index) => (
                    <p key={index}><b>User:</b> {msg.user} <br /><b>Bot:</b> {msg.bot}</p>
                ))}
            </div>
            <input value={input} onChange={(e) => setInput(e.target.value)} />
            <button onClick={sendMessage}>Send</button>
        </div>
    );
};

export default Chatbot;
