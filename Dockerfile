FROM python:3.8-slim-buster

RUN apt update && apt install libmediainfo-dev mediainfo libmediainfo-dev libmediainfo-doc gcc curl -y

RUN mkdir /blog
COPY . /blog
WORKDIR /blog/blog
RUN pip install -r /blog/requirements.txt

EXPOSE 8090

CMD python3 /blog/blog/main.py