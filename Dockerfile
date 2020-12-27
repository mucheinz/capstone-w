# python image
FROM python:3.8

RUN apt-get update && apt-get install -y \
python3-dev \
build-essential

# set working directory to /app
WORKDIR /app
ADD . /app

# install packages from file requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# make port 80 available to the world outside the container
EXPOSE 80

# run app.py when container launches
CMD ["python", "app.py"]

# docker build -t aavail .

