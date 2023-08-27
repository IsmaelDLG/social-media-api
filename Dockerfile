from python:3.11.4
# Set a dir for the app. Check if the parent dir exists before using
WORKDIR /usr/src/
# Docker "caches" steps, so installing requirements before copying the code will result in faster builds later on when only code changes
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
