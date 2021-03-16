# movie-database-webapp

## How to run
1. clone repo
2. create a python virtual environment. Please make sure to use python 3.9.1. This can be installed by running the following command  
   

   ``Python3 -m venv <NameOfEnviroment>``
   
3. Go to the root directory, activate the env and run the following command  

``pip install requirements.txt``

4. Change the `credentials.py` file to your msql password. Preferably link it to a credentials file to avoid sharing secrete information. 

5. To run the flask app run the following command

```python app.py ```

6. Open ` http://127.0.0.1:5000/` in the browser. 


Please do not use the current server in production as it is a dedicated development server. 


## Details
``app.py`` serves as the main entry point. This file contains two routes  

1.`write_your_own_query` This route serves a raw SQL query

2. `customizable` This route serve a parameterized SQL query. The query scenarios are in the`sql_queries.py` file. 