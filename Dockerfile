FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8080
ENV DJANGO_SUPERUSER_USERNAME admin
ENV DJANGO_SUPERUSER_PASSWORD admin
ENV DJANGO_SUPERUSER_EMAIL admin@smartdjangorest.tv
RUN chmod 664 .
RUN chmod +x run-app.sh
ENTRYPOINT ["/bin/bash", "/app/run-app.sh"]
