from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import json

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

# メインページ
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()

# チャットAPI
@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    user_message = request.message.strip()
    if not user_message:
        raise HTTPException(status_code=400, detail="Message is required")
    # モックアップの応答生成
    ai_response = f"AI Response to: {user_message}"
    return {"response": ai_response}
