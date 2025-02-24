import gradio as gr
from backend.gradio_english import demo_en
from backend.gradio_japanese import demo_jp
from backend.gradio_korean import demo_kr
import os

PORT_EN = int(os.getenv("GRADIO_PORT_EN", 7860))
PORT_JP = int(os.getenv("GRADIO_PORT_JP", 7861))
PORT_KR = int(os.getenv("GRADIO_PORT_KR", 7862))

if __name__ == "__main__":
    demo_en.launch(server_name="0.0.0.0", server_port=PORT_EN, share=False)
    demo_jp.launch(server_name="0.0.0.0", server_port=PORT_JP, share=False)
    demo_kr.launch(server_name="0.0.0.0", server_port=PORT_KR, share=False)
