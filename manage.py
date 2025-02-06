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
