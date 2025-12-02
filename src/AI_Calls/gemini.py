from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def generate_function(language, parameters, output, focus_mode, description):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f'Create a {language} function with the following parameters: {parameters} , \
            the function must have this output: {output}, \
            the focus mode chosen is {focus_mode}, \
            the user provided the following description {description}, \
            Provide only the function without any explanation'
    )
    
    return response.text
