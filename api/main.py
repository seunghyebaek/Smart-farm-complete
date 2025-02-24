from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import gradio as gr

# Gradio 페이지 import
from backend.gradio_english import demo_en
from backend.gradio_japanese import demo_jp
from backend.gradio_korean import demo_kr

app = FastAPI()
app.mount("/static", StaticFiles(directory="../client/assets"), name="static")

@app.get("/")
def read_root():
    return {"message": "Hello, This is the main app!"}

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
