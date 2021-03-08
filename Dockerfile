FROM python:3.8-slim-buster

RUN apt update && apt install libmediainfo-dev mediainfo libmediainfo-dev libmediainfo-doc gcc curl -y

RUN mkdir /blog
COPY ./blog /blog
WORKDIR /blog
RUN pip install -r /blog/requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
ENV PYTHONPATH=${PYTHONPATH}:/blog

EXPOSE 7331

CMD python3 /blog/blog/main.py