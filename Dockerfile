FROM python:3.9-buster

WORKDIR /api
RUN adduser --system api
USER api

COPY requirements.txt .
RUN pip3 install -r requirements.txt

EXPOSE 5000
COPY . .

CMD [ "python", "-m", "flask-server" ]