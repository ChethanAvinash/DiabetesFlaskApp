FROM chethan2606/keras-flask:latest 

WORKDIR /webapp

COPY . /webapp

EXPOSE 3000

CMD ["python3","app.py"]
