FROM python:3.13.7-alpine3.22
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app
CMD ["python3", "app.py"]