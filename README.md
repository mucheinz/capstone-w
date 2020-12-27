# IBM AI Enterprise Workflow Capstone
Files for the IBM AI Enterprise Workflow Capstone project. 

## Part 1

### 1. Case study part 1

run the AAVAIL.part1.ipynb Notebook


## Part 2


### 2. Baseline Model and Performance 

run the AAVAIL.part2.ipynb Notebook
    
### 3. train and test the model 

```bash
~$ python model.py
```

### 4. Run API test

```bash
~$ python app.py
```

```bash
~$ ! python unittests/APITests.py
```

### 5. Run all of the tests

```bash
~$ python runtests.py
```

### 6. Build docker container

```bash
~$ docker build -t aavail .
```

### 7. Run the Docker container

```bash
~$ docker run -p 8888:80 aavail
```

Navigate to http://0.0.0.0:8888/ 

