## TESTING CONTAINER

FROM python:3 as testing
WORKDIR /app

COPY setup.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install -e .[test]

VOLUME /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

## RELEASE container

FROM python:3 as release
WORKDIR /app

COPY setup.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install -e .

VOLUME /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
