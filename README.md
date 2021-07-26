# car_REST_API
Car REST_API 

There are two ways to open project: with Docker and without Docker.


USING DOCKER:
1. Download repository and install docker / docker-compose.
2. Move to 'netg' location and run: docker-compose up --build
3. Run migrations from Docker Level (docker-compose exec web python manage.py migrate)
4. <Optional> Create a superuser (docker-compose exec web python manage.py createsuperuser) to access admin panel (/admin/).
  
 WITHOUT DOCKER:
 1. Change line 91 in netg/settings.py to 
    'HOST': '127.0.0.1'
  2. Makemigrations and migrate (python3 manage.py makemigrations / python3 manage.py migrate)
  3. Run server (python3 manage.py runserver)
 ---------------------------------------------------------------------
  Deployed version:
  https://adriansuszek.pythonanywhere.com/cars/

   ---------------------------------------------------------------------
Endpoints, so you can test API:
  
  1. POST /cars/

Content-Type: application/json;charset=UTF-8

{

  "make" : "Volkswagen",

  "model" : "Golf",

}
  
  2. DELETE /cars/{  id }/
  
  
  3. POST /rate/

Content-Type: application/json;charset=UTF-8

{

  "car_id" : 1,

  "rating" : 5,

}
  
  4. GET /cars/
  
  5. GET /popular/
  
