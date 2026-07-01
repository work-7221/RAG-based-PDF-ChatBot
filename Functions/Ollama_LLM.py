import ollama

def generate_answer(prompt):
    client = ollama.Client(host='http://127.0.0.1:11434')
    response = client.chat(
        model="llama3.1",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]