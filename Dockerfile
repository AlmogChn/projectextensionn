FROM python:3-alpine
RUN pip install flask
RUN pip install PyMySQL
COPY db_connector.py /
COPY rest_app.py /
EXPOSE 5000
CMD ["python3", "./rest_app.py"]
