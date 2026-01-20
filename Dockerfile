FROM python:3.13-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "flask", "--app", "run" ,"run", "--host=0.0.0.0" ]