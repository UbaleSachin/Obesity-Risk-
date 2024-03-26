FROM python:3.11.7-slim-bookworm
COPY . /app
WORKDIR /app

RUN apt update -y && apt install awscli -y

ENV PYTHONPATH "${PYTHONPATH}:/src"

EXPOSE 5000

RUN pip install -r requirements.txt
CMD python app.py