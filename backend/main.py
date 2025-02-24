import os
from fastapi import FastAPI
import gradio as gr

# Gradio 페이지 import
from backend.gradio_english import demo_en
from backend.gradio_japanese import demo_jp
from backend.gradio_korean import demo_kr

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, This is the main app!"}

# Gradio 앱들을 개별 FastAPI 인스턴스로 마운트
app.mount("/korean", gr.mount_gradio_app(FastAPI(), demo_kr, path=""))
app.mount("/japanese", gr.mount_gradio_app(FastAPI(), demo_jp, path=""))
app.mount("/english", gr.mount_gradio_app(FastAPI(), demo_en, path=""))

