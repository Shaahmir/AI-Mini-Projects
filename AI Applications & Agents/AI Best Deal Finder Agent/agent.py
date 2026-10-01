import os
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
from tools import tools, handle_tool_calls
from prompts import SYSTEM_PROMPT

load_dotenv(override = True)

BASE_URL = "https://integrate.api.nvidia.com/v1"
API_KEY = os.getenv("NVIDIA_API_KEY")
MODEL_NAME = "nvidia/nemotron-3.5-lightning-30b-a3b"

client = OpenAI(
    base_url = BASE_URL,
    api_key = API_KEY
)

def call_agent(prompt, history: list[dict] | None = None):

    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history + [{"role": "user", "content": prompt}]
    
    response = client.chat.completions.create(
        model = MODEL_NAME,
        messages = messages,
        tools = tools
    )

    while response.choices[0].finish_reason == "tool_calls":
        
        message = response.choices[0].message
        tool_response = handle_tool_calls(message)
        messages.append(message)
        messages.extend(tool_response)
        
        response = client.chat.completions.create(
            model = MODEL_NAME,
            messages = messages
        )

    return response.choices[0].message.content

interface = gr.ChatInterface(
    fn = call_agent
)

interface.launch(
    inbrowser = True
)
