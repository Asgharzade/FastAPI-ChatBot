FROM python:3.12-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /home
COPY app /home/app
COPY misc /home/misc
COPY styles.html /home
EXPOSE 8000
ENTRYPOINT [ "uvicorn", "app.app:app", "--host", "0.0.0.0", "--reload" ]
