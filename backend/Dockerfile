FROM python:3.13.4-slim-bullseye

RUN python -m venv /opt/venv/
ENV PATH=/opt/venv/bin:$PATH

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./src .

# RUN echo "hello" > index.html
# docker run -it -p 8000:8000 py-app
CMD [ "python", "-m", "http.server", "8000" ]