FROM python:3-alpine
RUN pip install flask
COPY rest_app.py /
COPY combined_testing.py /
COPY clean_environment.py /
EXPOSE 5000
CMD ["python3", "./1.py"]
