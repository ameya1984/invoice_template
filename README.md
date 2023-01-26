# invoice_template
Invoice Management Template

# Setup virtual environment using 
$python3 -m venv ~/invoice

# Setup Project
Enable virtual environment
$source ~/invoice/bin/activate

$#cd <your_Workspace>
$cd ~/Workspace

$git clone https://github.com/ameya1984/invoice_template.git
$pip install -r requirements/requirements-prod.txt

# Setup Environment variable "ENVIRONMENT" as "development", "qa" or "production"

Setup values for DEBUG, SQLALCHEMY_DATABASE_URI, etc. 

# Setup dummy values in db and run project locally
$python setup.py
$python app.py

# Test apis locally

# Get Invoice by id
$curl http://localhost:5000/invoice/1

# Post Invoice
$curl -X POST -H "Content-Type: application/json" -d '{"date":"2022-01-01"}' http://localhost:5000/invoice/

# Get Invoice Items by id
$curl http://localhost:5000/invoice/1000000000 - Should get a exception message as record does not exists

# Post Invoice Items 
$curl -X POST -H "Content-Type: application/json" -d '{"units":10, "description": "New Item", amount:9.50}' http://localhost:5000/invoices_items/




