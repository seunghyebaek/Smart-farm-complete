# 🐍 FastAPI 실행 (Python 환경)
FROM python:3.9 AS backend

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]

# 🌐 Nginx 실행 (FastAPI와 연결)
FROM nginx:latest AS nginx

COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
