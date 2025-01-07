#!/bin/bash
# Description: Script to install the project dependencies
# Author: Manuel Ventura de Oliveira Neto

# 1. Create a virtual environment and activate it
python -m venv venv
source venv/Scripts/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set Flask environment variables
export FLASK_APP=run.py
export FLASK_ENV=development

# 4. Create a .env file
echo Creating .env file...
echo TOKEN_KEY=random_key > .env
echo EXP_TIME_MIN=30 >> .env
echo REFRESH_TIME_MIN=10 >> .env

# 5. Create the database using the Python from the virtual environment
./venv/Scripts/python -c "
from src.infra.config import *;
from src.infra.entities import *;
db_conn = DBConnectionHandler();
engine = db_conn.get_engine();
Base.metadata.create_all(engine)
"
