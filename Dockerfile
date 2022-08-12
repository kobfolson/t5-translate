FROM python:3.8-slim-buster

RUN mkdir /opt/model-data

ENV MODEL_DATA /opt/model-data

RUN apt-get update \
    && apt-get -y install wget --no-install-recommends \
    && apt-get clean

RUN wget https://huggingface.co/t5-base/raw/main/config.json -P ${MODEL_DATA}
RUN wget https://huggingface.co/t5-base/raw/main/tokenizer.json -P ${MODEL_DATA}
RUN wget https://huggingface.co/t5-base/resolve/main/pytorch_model.bin -P ${MODEL_DATA}

RUN mkdir /app

COPY . /app
COPY pyproject.toml /app

WORKDIR /app 

RUN pip3 install poetry==1.1.6
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]