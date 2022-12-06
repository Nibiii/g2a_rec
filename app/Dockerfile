FROM python:3.11-alpine

WORKDIR app

COPY ./ ./

RUN python3 -m pip install -r requirements.txt

RUN adduser -D flask && addgroup flask root

USER flask

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8080"]