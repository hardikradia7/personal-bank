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
    2. Run command install 'pip install pytest' or 'pip3 install fastapi'
    4. Go to personal-bank directory using command 'cd /path/to/personal-bank'.
    4. To execute tests run command 'pytest -v'

## 4. Some Sample Images for API Call and Unit test case execution

#### 1. Making API Call:

![validate_iban_rest_call](https://user-images.githubusercontent.com/78080557/170892669-febf34d5-e9f2-4a16-acc9-8dba3cae480c.png)

#### 2. Running unittest cases:

![pytest_sample_1](https://user-images.githubusercontent.com/78080557/170892689-d892b1f7-d61a-49ef-a4eb-641e97166d53.png)
![pytest_sample_2](https://user-images.githubusercontent.com/78080557/170892690-90d57614-c70e-4dc4-af9e-1f27ac736fe0.png)

