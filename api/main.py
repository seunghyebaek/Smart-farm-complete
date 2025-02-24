from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import gradio as gr

# FastAPI 앱 생성
app = FastAPI()

# 정적 파일 제공 (client/assets 폴더 내 파일을 `/static/` 경로에서 제공)
app.mount("/static", StaticFiles(directory="../client/assets"), name="static")

@app.get("/")
def read_root():
    return {"message": "Hello, This is the main app!"}

# Gradio 앱 마운트
@app.get("/korean")
async def korean():
    return gr.mount_gradio_app(app, demo_kr, path="/korean")

@app.get("/japanese")
async def japanese():
    return gr.mount_gradio_app(app, demo_jp, path="/japanese")

@app.get("/english")
async def english():
    return gr.mount_gradio_app(app, demo_en, path="/english")
