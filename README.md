# REQUIREMENT

#### Objective
Created a RESTful API using Python's Flask framework that interacts with MongoDb Compass. The API should follow the methods :- GET, POST, PUT, DELETE. And API should interact with Frontend.

####  Requirements

1. API Base Endpoint
    - The base endpoint for the API is /api/employee/.

2. Database
    - Uses MongoDb Compass.
    - the structure of the json is
      {
        "empid" : <Integer>,
        "name" : <String>,
        "designation" : <String>
      }

#### Steps to run the Program
1. Create a Virtual Enviornment
   - python -m venv employeeData 
2. Activate the env
    .\employeeData\Scripts\Activate.ps1
3. Install the below tools
    - pip install flask
    - pip install pymango
6. Execute the below command 
    - python app.py
