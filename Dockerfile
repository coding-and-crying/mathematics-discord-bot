FROM python:3.8.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt 
CMD python3 -u ./basic_mathematics_bot.py
