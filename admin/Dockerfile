FROM python:3.9.7-slim

COPY . /app
WORKDIR /app

RUN python3 -m venv /opt/venv
RUN pip install pip --upgrade 
RUN pip install -r /admin/requirements.txt 
RUN chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]