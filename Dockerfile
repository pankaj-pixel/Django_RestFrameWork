FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirments.txt /code/
RUN pip install -r requirments.txt

COPY . /code/



EXPOSE 8000

#cmd to run django server
CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]~