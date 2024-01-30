FROM python:3.11

WORKDIR /app
COPY haloart/requirements.txt /app
COPY . /app/
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt --no-cache-dir


CMD ["python", "manage.py", "runserver", "0:8000"]
