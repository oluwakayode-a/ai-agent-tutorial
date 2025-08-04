FROM python:3.13.4-slim-bullseye

WORKDIR /app

COPY ./src .

# RUN echo "hello" > index.html
# docker run -it -p 8000:8000 py-app
CMD [ "python", "-m", "http.server", "8000" ]