import os
from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel

# Initialize the OpenAI client using your environment variable
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

app = FastAPI()


class Request(BaseModel):
    text: str


@app.post("/")
async def ask(req: Request):
    # Sends the text to OpenAI's gpt-4o model
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": req.text}]
    )

    # Returning "reply" ensures the Noa app can successfully read and display the text
    return {"reply": response.choices[0].message.content}
  
