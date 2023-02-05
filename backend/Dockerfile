FROM python:3.7-alpine
WORKDIR /workdir
ENV FLASK_APP=flask-app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN apk add python3-dev libpq-dev
RUN pip3 install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]