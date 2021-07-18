FROM golang:1.17-rc

RUN go get -u github.com/streadway/amqp
RUN go get -u github.com/beego/bee/v2
RUN go get -u github.com/golang/protobuf/proto
RUN go get -u github.com/golang/protobuf/protoc-gen-go
RUN go get -u google.golang.org/grpc

EXPOSE 5002

CMD ["bee", "run"]