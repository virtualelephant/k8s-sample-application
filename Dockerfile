FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY publisher.py .
COPY publisher.sh .

RUN chmod +x publisher.sh

CMD ["/.publisher.sh"]
