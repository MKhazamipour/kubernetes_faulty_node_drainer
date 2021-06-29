FROM python:3.8-slim-buster


WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
RUN mv /app/kubectl /sbin
RUN chmod +x /sbin/kubectl

CMD [ "python3", "main.py" ]