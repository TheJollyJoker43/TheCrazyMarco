FROM python:3.9-alpine
WORKDIR /usr/src/app
RUN pip install -U discord.py
RUN pip install -U python-dotenv
