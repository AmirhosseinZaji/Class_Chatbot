import tiktoken

def chunk_transcript(transcript, max_tokens=4096):
    # Use a tokenizer that's compatible with OpenAI's models
    # A tokenizer is like a tool that breaks down text into smaller pieces (tokens) that the AI can understand
    # It's similar to how we break down sentences into words, but for AI
    tokenizer = tiktoken.get_encoding("cl100k_base")
    
    # Convert the transcript text into a list of token IDs
    # This is like translating our human language into a language the AI understands
    tokens = tokenizer.encode(transcript)
    
    # Initialize empty lists to store our chunks
    # Think of these as empty buckets where we'll put our text pieces
    chunks = []
    current_chunk = []

    # Iterate through each token in the transcript
    # This is like going through each word in the text one by one
    for token in tokens:
        # Add the token to the current chunk
        # We're filling up our current bucket with words
        current_chunk.append(token)
        
        # If the current chunk has reached or exceeded the maximum token limit
        # This is like checking if our bucket is full
        if len(current_chunk) >= max_tokens:
            # Convert the tokens back to text and add to the chunks list
            # We're sealing the full bucket and putting it aside
            chunks.append(tokenizer.decode(current_chunk))
            # Start a new chunk
            # We're grabbing a new empty bucket to start filling again
            current_chunk = []

    # If there are any remaining tokens in the current chunk, add them as the last chunk
    # This is like making sure we don't leave any words behind in a partially filled bucket
    if current_chunk:
        chunks.append(tokenizer.decode(current_chunk))

    # Return the list of text chunks
    # We're giving back all our filled buckets of text
    return chunks

# This function helps us break down a large transcript into smaller, more manageable pieces.
# Imagine you have a very long story, and you want to tell it to someone who can only listen for a short time.
# You'd break the story into smaller parts. That's what this function does with the transcript.
# This is important because many AI models have a limit on how much text they can process at once.
# By breaking the transcript into chunks, we can work with long transcripts without overwhelming the AI.
