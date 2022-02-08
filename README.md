# Sqlite db auto testing
The task:

1. Create db with "Ships" table containing 200 rows and 4 columns, 
"Engine" with 6 rows and 3 columns,
"Hulls" with 5 rows and 4 columns,
"Weapons" with 20 rows and 6 columns
There are Primary Key in last 3 tables
2. Need to create a test db from previous one and randomized every row in "Ships"
3. Compare each row in two tables and get a report

Pytest/Python


Use python 3.8 +
Create and activate virtual environments

```
python3 -m venv env
source env/bin/activate
```

Run in terminal

```
pip install -r requirements.txt
```

pre-commit https://pre-commit.com
```
pre-commit run --all-files
```

Run tests and get allure test report you can use:
```
pip install allure-pytest
pytest --alluredir=my_allure_results
allure serve my_allure_results
```
