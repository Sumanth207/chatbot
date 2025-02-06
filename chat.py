@app.post("/chat")
async def chat(user_input: str):
    if not user_input:
        raise HTTPException(status_code=400, detail="Input cannot be empty")

    bot_response = get_ai_response(user_input)
    save_chat_history(user_input, bot_response)

    return {"response": bot_response}
