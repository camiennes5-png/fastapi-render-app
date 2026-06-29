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
    # I have updated the model parameter below from "gpt-5.5" to "gpt-4o"
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": req.text}]
    )

    return {"answer": response.choices[0].message.content}
