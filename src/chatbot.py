from src.semantic_search import find_relevant_chunk
import re

def latex_to_unicode(text):
    # Replace LaTeX-style formulas with Unicode representations
    replacements = {
        r'\beta_0': 'β₀',
        r'\beta_1': 'β₁',
        r'\(': '',
        r'\)': '',
        r'\[': '',
        r'\]': '',
        r'\\': '',
    }
    for latex, unicode in replacements.items():
        text = text.replace(latex, unicode)
    return text

# New function to manage conversation history
def manage_conversation_history(history, query, response, max_history=5):
    history.append({"role": "user", "content": query})
    history.append({"role": "assistant", "content": response})
    # Keep only the last 'max_history' interactions
    return history[-max_history*2:]

def generate_response(query, chunks, chunk_embeddings, client, conversation_history=[]):
    # Find the most relevant chunk of the transcript for this query
    # This is like finding the most relevant page in a textbook for a specific question
    relevant_chunk = find_relevant_chunk(query, chunks, chunk_embeddings, client)
    
    # Prepare the messages including the conversation history
    messages = [
        {"role": "system", "content": "You are a helpful assistant. When explaining mathematical concepts, use simple Unicode representations instead of LaTeX. For example, use β₀ instead of \\beta_0. Provide detailed explanations with examples when possible. Remember previous context when answering new questions."},
    ] + conversation_history + [
        {"role": "user", "content": f"Based on the following lecture material and our previous conversation, answer the question in detail: {relevant_chunk}\nQuestion: {query}\nAnswer:"}
    ]
    
    # Use OpenAI's chat completion API to generate a response
    # This is like asking a very smart AI teacher to answer the question based on the relevant textbook page
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",  # This is the AI model we're using to generate the response
        messages=messages,
        max_tokens=500  # Increased from 150 to 500 to allow for longer, more detailed responses
    )
    
    # Convert any remaining LaTeX-style formulas to Unicode
    formatted_response = latex_to_unicode(response.choices[0].message.content.strip())
    return formatted_response

def handle_query(query, chunks, chunk_embeddings, client, conversation_history=[]):
    # Generate a response to the query
    # This is the main function that processes a question and gets an answer
    response = generate_response(query, chunks, chunk_embeddings, client, conversation_history)
    
    # If the AI couldn't find a good answer, return a default message
    # This is like having a backup response if the AI isn't sure about the answer
    if "I don't know" in response or response.strip() == "":
        return "This question falls outside the course material.", conversation_history
    
    # Update conversation history
    updated_history = manage_conversation_history(conversation_history, query, response)
    
    # Otherwise, return the generated response
    # If the AI found a good answer, we give that answer to the user
    return response, updated_history

# These functions handle the process of answering a question based on the transcript.
# Imagine you're a teacher's assistant. When a student asks a question:
# 1. You first find the most relevant part of the textbook (find_relevant_chunk).
# 2. Then you carefully read that part and formulate a detailed answer (generate_response).
# 3. If you're confident in your answer, you give it to the student. If not, you tell them it's not covered in the course (handle_query).
# This process helps ensure that we always provide a response, even if the question is not directly covered in the transcript.
