FROM python:3.9-slim

WORKDIR /.

COPY . .
RUN pip install -r requirements.txt

RUN chmod +x ./entrypoint.sh
EXPOSE 8000
ENTRYPOINT ["sh", "entrypoint.sh"]
