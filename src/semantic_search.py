import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def find_relevant_chunk(query, chunks, chunk_embeddings, client):
    # Create an embedding for the query
    # This converts the question into the same special number format as our transcript chunks
    # It's like translating the question into the same secret code language we used for the transcript
    query_embedding = client.embeddings.create(
        model="text-embedding-ada-002",
        input=query
    ).data[0].embedding

    # Calculate the cosine similarity between the query embedding and all chunk embeddings
    # Cosine similarity measures how similar two vectors are, which in this case represents semantic similarity
    # Imagine measuring how close the angle is between two arrows pointing in different directions
    # The more similar the meaning, the closer the arrows point in the same direction
    similarities = cosine_similarity([query_embedding], chunk_embeddings)
    
    # Find the index of the chunk with the highest similarity to the query
    # This is like finding which arrow points most closely in the same direction as our question arrow
    most_relevant_index = np.argmax(similarities)
    
    # Return the text of the most relevant chunk
    # We're picking out the paragraph that best matches the question
    return chunks[most_relevant_index]

# This function helps us find which part of the transcript is most relevant to the question being asked.
# Imagine you have a library of books (our transcript chunks), and you're trying to find which book best answers a specific question.
# Instead of reading every book, we've given each book a special code (embedding) that summarizes its content.
# We also turn the question into a similar code.
# Then, we compare the question's code to every book's code and pick the book with the most similar code.
# This helps us quickly find the most relevant information without having to read everything in detail.
