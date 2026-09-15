FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
# ➡️ Copy your requirements.txt from your computer into /app.

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# ➡️ Copy your whole project code into the container.

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]






# Give me Python → create /app → copy my requirements → install them → copy my code → expose 8000 → start FastAPI."



