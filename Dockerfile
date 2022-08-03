FROM python:3-alpine
RUN pip install flask
COPY rest_app.py /
EXPOSE 5000
CMD ["python3", "./rest_app.py"]
