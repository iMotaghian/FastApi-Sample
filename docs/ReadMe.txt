# 1-2 [] make main.py // make venv:
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
