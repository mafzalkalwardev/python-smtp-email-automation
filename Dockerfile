FROM alpine:3.20
WORKDIR /src
COPY . .
LABEL org.opencontainers.image.source="https://github.com/mafzalkalwardev/python-smtp-email-automation"
CMD ["sh", "-c", "echo 'python-smtp-email-automation source package' && ls -1"]
