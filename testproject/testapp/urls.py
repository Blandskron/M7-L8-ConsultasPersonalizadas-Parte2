from django.urls import path
from . import views

urlpatterns = [
    path('my_table/', views.my_table_view, name='my_table'),
]
