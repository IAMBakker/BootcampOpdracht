FROM python:3.6-alpine

COPY . /exercise

WORKDIR /exercise

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["./exercises/exerciseOne.py"]