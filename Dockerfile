FROM python:3.11.4-slim
WORKDIR G:\fruits_and_platns_classification
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
