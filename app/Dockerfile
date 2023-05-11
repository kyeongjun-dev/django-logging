FROM python:3.9-slim
RUN pip install --upgrade pip && pip install django
RUN mkdir -p /var/log/django
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
