FROM golang:1.24-alpine AS builder

RUN go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

FROM python:3.10-alpine

RUN apk update

COPY --from=builder /go/bin/subfinder /usr/local/bin/subfinder

RUN chmod +x /usr/local/bin/subfinder

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN apk add --no-cache curl

COPY app.py /home/app.py

CMD ["python", "/home/app.py"]
