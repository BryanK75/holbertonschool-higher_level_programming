# Use the Alpine base image
FROM alpine:latest

# Install curl
RUN apk add --no-cache curl

# Create a directory for your app
RUN mkdir -p /app

# Copy the config.txt file into the container
COPY config.txt /app/config.txt

# Specify the command to run when the container starts
CMD ["echo", "Hello, World!"]
