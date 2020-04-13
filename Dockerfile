FROM python:3.7.6
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
CMD python3 application.py