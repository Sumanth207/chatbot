Simple AI-Powered Customer Support Chatbot
This chatbot uses OpenAI's GPT-3.5 (or GPT-4) to handle basic customer queries like product information and order status.

Tech Stack

Backend: FastAPI (Python)

AI Model: OpenAI’s GPT-3.5 (via OpenAI API)

Database: MongoDB (for storing chat history)

Frontend: React.js (for UI)

Implementation Steps


1. Setup the Environment
Install necessary dependencies:

pip install fastapi uvicorn openai pymongo python-dotenv


2. Build the Backend (FastAPI)

2.1 Import Dependencies & Initialize App

from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["chatbot"]
chat_collection = db["chats"]

# Initialize OpenAI client
openai_client = OpenAI(api_key=OPENAI_API_KEY)


2.2 Generate Chatbot Responses

def get_ai_response(user_query):
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_query}]
    )
    return response.choices[0].message["content"]


2.3 Store Chat History in MongoDB

def save_chat_history(user_message, bot_response):
    chat_collection.insert_one({"user": user_message, "bot": bot_response})


2.4 Define API Endpoint for Chatbot

@app.post("/chat")
async def chat(user_input: str):
    if not user_input:
        raise HTTPException(status_code=400, detail="Input cannot be empty")

    bot_response = get_ai_response(user_input)
    save_chat_history(user_input, bot_response)

    return {"response": bot_response}


3. Build the Frontend (React.js)


3.1 Install Dependencies

npx create-react-app chatbot-ui
cd chatbot-ui
npm install axios

3.2 Create Chatbot UI Component

Chatbot.js

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


4. Deployment

Backend: Deploy using Render or AWS Lambda.

Frontend: Deploy with Vercel or Netlify.

GitHub Repository

Upload your project to GitHub:

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/chatbot.git
git push -u origin main
