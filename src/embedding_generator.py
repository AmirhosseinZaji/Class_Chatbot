from openai import OpenAI
import os

def generate_embeddings(chunks, client):
    # Initialize an empty list to store our embeddings
    # Think of this as preparing an empty notebook to write down special codes
    embeddings = []
    
    # For each chunk of text in our chunks list
    # Imagine we're going through each paragraph of a story
    for chunk in chunks:
        # Use the OpenAI API to create an embedding for this chunk
        # An embedding is like a secret code that represents the meaning of the text
        # It's as if we're translating each paragraph into a special language only computers understand
        response = client.embeddings.create(
            model="text-embedding-ada-002",  # This is the OpenAI model used for creating embeddings
            input=chunk  # The text chunk we want to create an embedding for
        )
        
        # Extract the embedding from the API response and add it to our list
        # We're writing down the secret code for each paragraph in our notebook
        embeddings.append(response.data[0].embedding)
    
    # Return the list of embeddings
    # We're giving back our notebook full of secret codes, one for each paragraph
    return embeddings

# This function takes a list of text chunks and converts each one into an embedding.
# Imagine you have a magic translator that can turn any piece of text into a long list of numbers.
# These numbers (embeddings) somehow capture the meaning of the text.
# Embeddings are useful because they allow us to measure how similar two pieces of text are, even if they use different words.
# For example, "The cat sat on the mat" and "A feline rested on the rug" would have similar embeddings.
# We'll use these embeddings later to find which part of the transcript is most relevant to a given question.
