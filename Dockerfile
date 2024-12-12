FROM python:3.9-alpine
EXPOSE 5000
EXPOSE 6000
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "flask", "run" ]

