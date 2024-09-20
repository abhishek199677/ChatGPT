from dotenv import load_dotenv
import os
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_gpt_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        return response.choices[0].message['content']
    except openai.error.RateLimitError:
        return "Sorry, I've reached my daily limit. Please try again later."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def chat():
    print("Welcome to the AI Chatbot!")
    print("Type 'exit' to quit the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("chatbot: Goodbye!")
            break
        
        response = get_gpt_response(user_input)
        print("chatbot: ", response)

if __name__ == "__main__":
    if openai.api_key is None:
        print("Error: OPENAI_API_KEY is not set in the environment.")
        exit(1)
    
    chat()
