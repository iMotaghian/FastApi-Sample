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
# make def for get value from endpoint