# Project: invoice_template
## _Invoice Management Template_

## Installation
Setup virtual environment using venv 
```python3 -m venv ~/invoice```

Setup Project
Enable virtual environment
```source ~/invoice/bin/activate```

Clone Project
```cd ~/Workspace
   git clone https://github.com/ameya1984/invoice_template.git
   cd invoice_template
   pip install -r requirements/requirements-prod.txt
```

Setup Environment variable "ENVIRONMENT" as "development", "qa" or "production"
```export ENVIRONMENT=development```

Setup values for DEBUG, SQLALCHEMY_DATABASE_URI in env/development

Setup dummy values in db and run project locally
```python setup.py```

## Run project locally
```python app.py```

Test apis locally

- Get JWT access token
```
curl -X POST -H "Content-Type: application/json" http://localhost:5000/login/ -d'{"username":"invoice_app", "password":"invoice_app"}'
```
- Set TOKEN in environment. for e.g.
```
export TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3NDg4NjMzNCwianRpIjoiMDE3MjRhZGUtODY5YS00YWQ1LThjMWEtMDcxMDE5OGI4ZDE1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imludm9pY2VfYXBwIiwibmJmIjoxNjc0ODg2MzM0LCJleHAiOjE2NzQ4ODk5MzR9._9XlRqll3AAdqdbB1LLuOchuQPN86qGzNbKuOIbY7X4
```

- Get Invoice by id
```
curl http://localhost:5000/invoice/5 -H "Authorization: Bearer $TOKEN"
curl http://localhost:5000/invoice?id=5 -H "Authorization: Bearer $TOKEN"
```

- Get Invoice Items by id - Should get a error message as record does not exists
```
curl http://locialhost:5000/invoice/1000000000 -H "Authorization: Bearer $TOKEN"
```

- Post Invoice
```
curl -X POST -H "Content-Type: application/json" -d '{"date": "2023-01-26 00:12:35", "items": [{"units":1, "description":"pen", "amount":5}, {"units":5, "description": "pencil", "amount":2.5}]}' http://localhost:5000/invoice -H "Authorization: Bearer $TOKEN"
```

- Get Invoice Items by id
```
curl http://localhost:5000/invoices_items/30 -H "Authorization: Bearer $TOKEN"
curl http://localhost:5000/invoices_items?id=30 -H "Authorization: Bearer $TOKEN"
```

- Post Invoice Items to update invoice 
```
curl -X POST http://localhost:5000/invoices_items -H "Authorization: Bearer $TOKEN" -d '{"units":10, "description":"books", "amount":15, "invoice_id": 9}'
```


