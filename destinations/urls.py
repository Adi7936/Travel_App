from django.urls import path
from . import views
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
   
    path('destinations/', views.DestinationListCreate.as_view(), name='destination-list-create'),
    path('destinations/<int:pk>/', views.DestinationRetrieveUpdateDestroy.as_view(), name='destination-retrieve-update-destroy'),
]
