# Punyurl  
**Punyurl** is a URL shortener app built using Python and Django. The database used is SQLite.

Project homepage: http://127.0.0.1:8000/punyurl/

## Installation

1.	**Python**: This application was developed using python 3.10.2 in pycharm IDE. Please install preferably the same version. 

2.	Change to directory containing requirements.txt and install the python packages mentioned in it using the below command: 

```
pip install -r requirements.txt
```

3.	 The database used is **SQLite** which is by default supported by python and Django. 
Change to directory containing manage.py and run below 2 commands to get the database ready:  

```
python manage.py makemigrations  
python manage.py migrate
```

4.	Start the application by running the below command:

```
python manage.py runserver
```

5. The application is hosted by default on localhost server. Load the url http://127.0.0.1:8000/punyurl/ on a browser. 

