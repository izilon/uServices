FROM python:3.8
MAINTAINER Your Name "rsiqueira"

WORKDIR /app

# We copy just the requirements.txt first to leverage Docker cache
COPY . /app

RUN pip install -r requirements.txt
RUN ls -ls /app

#COPY app.py /app

ENTRYPOINT [ "python" ]

CMD ["app.py" ]
