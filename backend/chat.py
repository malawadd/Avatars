import os

from fastapi import FastAPI
from swarmzero import Agent
from dotenv import load_dotenv
from typing import Optional, List
import asyncio

load_dotenv()

app = FastAPI()

def get_config_path(filename):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), filename))

def get_image_path(filename):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), filename))

my_agent = Agent(
    name="my_agent",
    functions=[],
    instruction="you're good assistance, your replies should be three sentences max",
    config_path=get_config_path("swarmzero_config.toml"),
)

@app.get("/chat")
async def chat_endpoint(prompt: str, image_filename: Optional[str] = None):
    # Define the image path if provided
    image_paths = [get_image_path(image_filename)] if image_filename else []
    
    # Call the chat method with the prompt and optional image
    res = await my_agent.chat(
        prompt=prompt,
        image_document_paths=image_paths
    )
    
    return {"response": res}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5450)
