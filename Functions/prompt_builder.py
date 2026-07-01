def build_prompt(question, context):
    prompt = f"""
            You are a helpful AI assistant.

            Answer ONLY the user's question.

            Question:
            {question}

            Context:
            {context}
    """

    return prompt