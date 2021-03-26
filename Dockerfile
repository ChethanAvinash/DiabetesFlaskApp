FROM chethan2606/keras-flask:latest 

WORKDIR /webapp

COPY . /webapp

EXPOSE 3000

ENTRYPOINT ['python3']

CMD ['app.py']

