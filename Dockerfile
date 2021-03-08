FROM python:3.8-slim-buster

RUN apt update && apt install libmediainfo-dev mediainfo libmediainfo-dev libmediainfo-doc gcc curl -y

RUN mkdir /blog
WORKDIR /blog/blog
COPY . /blog
RUN pip install -r requirements.txt

EXPOSE 8090

CMD python3 /blog/main.py