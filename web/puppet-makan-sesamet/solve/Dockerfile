FROM golang:1.18-alpine
WORKDIR /usr/src/app
COPY . .
RUN go build -o server
EXPOSE 45000
ENTRYPOINT [ "/usr/src/app/server" ]

