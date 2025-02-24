from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import gradio as gr

# Gradio 앱 가져오기
from api.gradio_korean import demo_kr
from api.gradio_japanese import demo_jp
from api.gradio_english import demo_en

# FastAPI 앱 생성
app = FastAPI()

# 정적 파일 제공 (client/assets 폴더 내 파일을 `/static/` 경로에서 제공)
app.mount("/static", StaticFiles(directory="client/assets"), name="static")

@app.get("/")
def read_root():
    return {"message": "Hello, This is the main app running on Render!"}

# Gradio 앱 마운트 (FastAPI 내부에 Gradio UI 포함)
app.mount("/korean", gr.mount_gradio_app(app, demo_kr, path="/korean"))
app.mount("/japanese", gr.mount_gradio_app(app, demo_jp, path="/japanese"))
app.mount("/english", gr.mount_gradio_app(app, demo_en, path="/english"))
