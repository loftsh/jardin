FROM python:3

WORKDIR /app

COPY setup.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install -e .

VOLUME /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
