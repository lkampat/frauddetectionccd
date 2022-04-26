from django.urls import path
from . import views
urlpatterns=[
    path("", views.home, name="index"),
    path('download',views.models),
    path('upload.php',views.model_data),
    path('Data_set',views.Data_set),


   ]
