# Educational AI Chatbot Assistant

## Overview
This AI-powered chatbot is designed to help faculty create personalized teaching assistants for their courses. The chatbot can understand your course materials and answer student questions accurately, providing detailed explanations while maintaining context throughout conversations.

## Features
- 📚 Processes any course material (lectures, notes, slides)
- 💬 Answers student questions with detailed explanations
- 🧮 Handles mathematical formulas and technical content
- 🔄 Maintains conversation context for follow-up questions
- 📝 Provides relevant examples from course materials

## Prerequisites
Before starting, you'll need:
1. A computer with Python installed (version 3.8 or higher)
2. An OpenAI API key (obtain from [OpenAI's website](https://platform.openai.com))
3. Basic familiarity with using the command line/terminal

## Step-by-Step Setup Guide

### 1. Initial Setup

#### Install Python
1. Visit [Python's official website](https://www.python.org/downloads/)
2. Download and install Python for your operating system
3. Verify installation by opening terminal/command prompt and typing:
   ```bash
   python --version
   ```

#### Get OpenAI API Key
1. Go to [OpenAI's platform](https://platform.openai.com)
2. Create an account or sign in
3. Navigate to API keys section
4. Create a new secret key
5. Copy the key (you'll need it later)

### 2. Project Setup

#### Download the Project
1. Download this project as a ZIP file
2. Extract it to a folder on your computer
3. Open terminal/command prompt
4. Navigate to the project folder:
   ```bash
   cd path/to/your/folder
   ```

#### Install Required Packages
Copy and paste this command into your terminal:
```bash
pip install openai tiktoken python-dotenv
```

#### Configure API Key
1. In the project folder, create a new file named `.env`
2. Open it with any text editor
3. Add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
   Replace `your_api_key_here` with your actual API key

### 3. Prepare Your Course Material

#### Format Your Content
1. Create a text file named `transcript.txt`
2. Add your course material to this file
3. You can include:
   - Lecture transcripts
   - Course notes
   - Reading materials
   - Assignment instructions
   - Example problems and solutions

Example format:
```text
Topic: Introduction to Linear Algebra

Lecture 1: Vectors and Matrices

Key Concepts:
1. Vectors are quantities with both magnitude and direction
2. Matrices are rectangular arrays of numbers
...

Examples:
1. Consider a vector v = [3, 4]
...
```

### 4. Running the Chatbot

#### Start the Program
1. Open terminal/command prompt
2. Navigate to the project folder
3. Run the program:
   ```bash
   python main.py
   ```

#### Using the Chatbot
1. Wait for the "Ready to answer questions!" message
2. Type your question and press Enter
3. The chatbot will respond based on your course material
4. Type 'exit' to end the session

Example interaction:
```
Welcome to the AI Chatbot!
Loading and processing the transcript...
Transcript processed. Ready to answer your questions!

Your question: What is a vector?
AI: Based on the course material, a vector is a quantity that has both magnitude 
and direction. Let me explain this with an example...

Your question: Can you give another example?
AI: Of course! Building on our previous discussion...
```

## Customization Options

### Adjusting Response Length
In `src/chatbot.py`, find:
```python
max_tokens=500  # Increase for longer responses
```

### Modifying System Behavior
In `src/chatbot.py`, customize the system prompt:
```python
system_prompt = """You are a helpful teaching assistant for [YOUR_COURSE].
Please explain concepts using [SPECIFIC_APPROACH]..."""
```

## Troubleshooting

### Common Issues and Solutions

1. **"API key not found" error**
   - Check if `.env` file exists
   - Verify API key is correctly copied
   - Make sure there are no spaces around the API key

2. **"Module not found" error**
   - Run `pip install [module_name]`
   - Make sure you're in the correct folder

3. **Chatbot gives irrelevant answers**
   - Check `transcript.txt` formatting
   - Add more context to your course material
   - Make questions more specific

## Cost Management

The chatbot uses OpenAI's API, which has associated costs:
- Embeddings: ~$0.0001 per 1K tokens
- GPT-4: ~$0.03 per 1K tokens

Tips to manage costs:
1. Monitor usage through OpenAI dashboard
2. Set usage limits in OpenAI account
3. Use shorter chunks of text when possible
4. Cache responses for common questions

## Support and Updates

For technical support:
1. Check the troubleshooting section
2. Review OpenAI's documentation
3. Contact your IT department

## Best Practices

1. **Content Organization**
   - Structure course material clearly
   - Include plenty of examples
   - Use consistent formatting

2. **Usage Guidelines**
   - Test with sample questions first
   - Monitor student interactions
   - Regularly update course material

3. **Security**
   - Keep API key secure
   - Don't share `.env` file
   - Regularly rotate API key

## Future Improvements

Planned features:
- Multiple file support
- Web interface
- Student usage analytics
- Response customization options

## Contributing

We welcome suggestions for improvements! Please share your feedback and ideas for making this tool more useful for education.
