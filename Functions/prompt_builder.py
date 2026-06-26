def build_prompt(question, context):
    return f"""
    You are an AI assistant.
    Your task is to give answer to using below aspects along with your insights.
    
    Question: {question}
    Context: {context}
    Answer: 
    """