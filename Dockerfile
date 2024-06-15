FROM python:3.10-slim as python310
WORKDIR /code
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

FROM python:3.11-slim-bookworm as python311
WORKDIR /code
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .