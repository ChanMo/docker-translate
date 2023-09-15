FROM alpine:latest

COPY repositories /etc/apk/repositories

RUN apk add bash gawk curl less hunspell python3 py3-pip && rm -rf /var/cache/apk/*
COPY trans /bin

RUN pip3 install flask gunicorn
WORKDIR /app

EXPOSE 5000
COPY app.py .

CMD ["gunicorn", "-w", "4", "-b", ":5000", "app:app"]

