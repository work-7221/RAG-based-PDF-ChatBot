def build_prompt(question, context, ongoing):
    prompt = f"""
        You are a helpful AI assistant.

        Answer ONLY the user's question.

        Question:
        {question}

        Context:
        {context}

        On-going Context:
        {ongoing}
    """

    return prompt