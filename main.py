from openai import OpenAI
import os
from dotenv import load_dotenv
from src.transcript_processor import chunk_transcript
from src.embedding_generator import generate_embeddings
from src.semantic_search import find_relevant_chunk
from src.chatbot import handle_query

# Load environment variables from .env file
# This allows us to securely store and access sensitive information like API keys
# Environment variables are like secret settings for our program
load_dotenv()

# Create an OpenAI client
# This client is like a messenger that helps us talk to OpenAI's smart AI
# We use the API key (like a secret password) to prove we're allowed to use the AI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def main():
    print("Welcome to the AI Chatbot! I'm here to answer your questions about the lecture material.")
    print("Loading and processing the transcript...")

    # Read the entire content of the transcript file
    # This file contains the lecture material that we'll use to answer questions
    # It's like opening a textbook and reading all the pages
    with open("transcript.txt", "r") as file:
        transcript = file.read()
    
    # Break down the transcript into smaller, manageable chunks
    # Imagine cutting a long piece of text into smaller paragraphs
    # This is necessary because there might be a limit on how much text we can process at once
    chunks = chunk_transcript(transcript)
    
    # Generate embeddings for each chunk of the transcript
    # Embeddings are like secret codes that represent the meaning of each chunk
    # They help the computer understand the content of the text
    chunk_embeddings = generate_embeddings(chunks, client)
    
    print("Transcript processed. Ready to answer your questions!")
    print("Type 'exit' at any time to end the conversation.")
    print("\n---\n")

    # Initialize an empty conversation history
    conversation_history = []
    
    while True:
        # Get user input
        query = input("Your question: ")
        
        if query.lower() == 'exit':
            print("Thank you for using the AI Chatbot. Goodbye!")
            break
        
        # Process the query and generate a response
        response, conversation_history = handle_query(query, chunks, chunk_embeddings, client, conversation_history)
        
        # Display the generated response
        print("\nAI: ", response)
        print("\n---\n")

# This is a common Python idiom to ensure that the main() function only runs if this script is executed directly
# It's like saying "only start the program if someone clicks on it directly"
if __name__ == "__main__":
    main()
