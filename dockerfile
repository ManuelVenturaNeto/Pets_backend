
FROM python:3.13.1-slim

ENV TZ=America/Sao_Paulo

WORKDIR /app

ENV FLASK_APP run.py

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]