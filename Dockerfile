FROM python:3.7-slim
WORKDIR /usr/src/app
COPY . .
ENV GOOGLE_APPLICATION_CREDENTIALS "dev-service-account.json"
RUN python -m pip install -r requirements.txt
EXPOSE 5001
CMD ["python","main.py"]