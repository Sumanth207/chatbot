def get_ai_response(user_query):
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_query}]
    )
    return response.choices[0].message["content"]
