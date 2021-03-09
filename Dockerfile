FROM python:3.8-slim-buster

RUN apt update && apt install libmediainfo-dev mediainfo libmediainfo-dev libmediainfo-doc gcc curl -y

RUN mkdir /blog
COPY . /blog
WORKDIR /blog
RUN pip install poetry -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
RUN poetry shell
RUN poetry install
#RUN pip install -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
ENV PYTHONPATH=${PYTHONPATH}:/blog

EXPOSE 7331

CMD python3 blog/main.py