# 1-2 [ّFastAPI] make main.py // make venv:
py -m venv env
# active venv
env\Scripts\activate.ps1
# install fast api
pip install fastapi
# need uvicorn for run api (vserver)
pip install uvicorn
# update main.py >> say hello : world
# run server with "uvicorn"
uvicorn main:app --reload
# localhost:8000

# 2-2 [Swagger] API Documentation:
http://127.0.0.1:8000/docs

# 2-3 [POST / GET] update main.py
# make def (aboutGetName) for get value from endpoint
# make def (getList) for get list
# make def (addToList) for POST method

# 2-4 [PUT / DELETE] make (updateList) for put method
# make (deleteFromList) for delete method

# 3-1 [DB] -> https://docs.sqlalchemy.org/en/20/intro.html#installation
pip install SQLAlchemy

# 3-2 [Class Model] make class (mySchoolClasses)
# set DB: make database.py

# 3-3 [make model database] make models.py
# import models in main.py
# read_school_class

# 3-4 [make file and connect to DB] read_school_class 
# get.post create_school_class

# 3-5 []