
A REST API App Using django and djangorestframework (DRF).

How to setup?
  
  python -m venv env
  
  git clone the project
  
  run: pip install -r requirements.txt
  
  
  run: python ./manage.py makemigrations
  run: python ./manage.py migrate
  
Ready to deploy direclty on Heroku.

POST /cars/ for adding a car.

DELETE /cars/{id} for deleting a car by ID.

GET /cars/ for fetching cars and average rating.

POST /rate/ for adding a rate to the car.

GET /popular/ for fetching and oredring car by how many times a car been rated.
