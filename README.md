# car_REST_API
Car REST_API 


Below are steps to run API locally:
1. Download repository and install docker / docker-compose.
2. Run: docker-compose up --build
3. Run migrations from Docker Level (docker-compose exec web python manage.py migrate)
4. <Optional> Create a superuser (docker-compose exec web python manage.py createsuperuser) to access admin panel (/admin/).
