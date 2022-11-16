FROM python:3.9.7-slim


COPY . /app

WORKDIR /app
COPY admin/requirements.txt /app/requirements.txt

RUN python3 -m venv /opt/venv
RUN pip install pip --upgrade && \
    pip install -r requirements.txt && \
    chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]