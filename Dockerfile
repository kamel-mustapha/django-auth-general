FROM python:3.13-alpine

WORKDIR /app/

COPY ./requirements.txt ./requirements.txt 

RUN python -m pip install --upgrade pip \
    && pip install -r requirements.txt 

COPY . .

CMD ["sh", "start-server.sh"]
