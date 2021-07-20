from django.urls import path
from .views import car_list, car_detail, rates, popular
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('cars', views.CarListView)


urlpatterns = [
    path('cars/', car_list),
    path('cars/<int:car_id>', car_detail),
    path('rate/', rates),
    path('popular/', popular),
    # path('average/', average)

    # path('', include(router.urls))
]
