FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUMBUFFERED 1

WORKDIR /usr/src/dm_rest

COPY ./requirements.txt usr/src/requirements.txt
RUN pip install -r usr/src/requirements.txt

COPY . /usr/src/dm_rest

EXPOSE 8000