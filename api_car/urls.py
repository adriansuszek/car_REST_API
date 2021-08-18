from django.urls import path
from rest_framework import routers

from .views import car_list, car_detail, rates, popular

router = routers.DefaultRouter()
# router.register('cars', views.CarListView)


urlpatterns = [
    # path('cars/', car_list),
    path('', car_list),
    path('cars/<int:car_id>', car_detail),
    path('rate/', rates),
    path('popular/', popular),
    # path('average/', average)

    # path('', include(router.urls))
]
