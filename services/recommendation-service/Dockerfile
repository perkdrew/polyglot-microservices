FROM python:3.8-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV VIRTUAL_ENV /opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH $VIRTUAL_ENV/bin:$PATH

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update \
    && apt-get install netcat gcc -y \
    && apt-get clean

RUN pip install --upgrade pip --no-cache-dir -r /app/requirements.txt 

COPY . /app/

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "5001"]