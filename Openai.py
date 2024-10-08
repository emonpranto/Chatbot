import openai
import os
import time
from dotenv import load_dotenv
from openai.error import RateLimitError, APIError

load_dotenv()

openai.api_key = os.getenv('openai_api_key')

def Chat_With_Gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': prompt}]
        )
        return response.choices[0].message.content.strip()
    except RateLimitError:
        print("Rate limit exceeded. Please wait before retrying.")
        time.sleep(60)  # wait for 1 minute before retrying
        return "Please try again later."
    except APIError as e:
        return f"API error: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "goodbye", 'exit', 'tata']:
            break
        response = Chat_With_Gpt(user_input)
        print("Moucha: ", response)
