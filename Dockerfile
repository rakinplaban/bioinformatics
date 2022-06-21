FROM python:3
COPY . /bioinformatics
RUN pip install -r requirements.txt
CMD ["python3","manage.py" ,"runserver","127.0.0.1:8000"]