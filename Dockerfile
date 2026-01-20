FROM python:3.13-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY . .

CMD [ "flask", "--app", "run" ,"run", "--host=0.0.0.0", "--port=5000" ]