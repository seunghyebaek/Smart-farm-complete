import sys
import os
from fastapi import FastAPI
import gradio as gr

# backend 폴더를 Python 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Gradio 페이지 import
from backend.gradio_english import demo_en
from backend.gradio_japanese import demo_jp
from backend.gradio_korean import demo_kr

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello This is main app!"}

# Gradio 앱들을 개별 FastAPI 인스턴스로 마운트
app.mount("/korean", gr.mount_gradio_app(FastAPI(), demo_kr, path=""))
app.mount("/japanese", gr.mount_gradio_app(FastAPI(), demo_jp, path=""))
app.mount("/english", gr.mount_gradio_app(FastAPI(), demo_en, path=""))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
