FROM python:3
WORKDIR /app
COPY . .
RUN python3 -m pip install -U discord.py python-decouple
CMD python -u ./basic_mathematics_bot.py
