# Personal Bank

## APIs supported:
  #### POST /api/v1/ibans/validate

## 1. Instructions to deploy this service as docker container:

    1. Go to personal-bank directory using command 'cd /path/to/personal-bank'.
    2. Create a docker image with help of Dockerfile using command 'docker build -t personal-bank:v1.0 .'.
    3. Run docker image using command 'docker run -dp 8000:8000 personal-bank:v1.0'

## 2. Make api calls on validate iban endpoint:

    1. In any rest api client set url as 'http://<ip-address>:8000/api/v1/ibans/validate'
    2. set method as POST
    3. set JSON request body as {"iban": <iban-string>}


## 3. Running unit test cases on local environment:
    1. Run command install 'pip install pytest' or 'pip3 install pytest'
    2. Go to personal-bank directory using command 'cd /path/to/personal-bank'.
    3. To execute tests run command 'pytest -v'
