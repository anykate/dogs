from django.urls import path
from . import views

app_name = 'dog_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),

    # Ensure no spacing in between '<int:' and 'dog_id>/'
    path('edit/<int:dog_id>/', views.edit, name='edit'),

    # Ensure no spacing in between '<int:' and 'dog_id>/'
    path('update/<int:dog_id>/', views.update, name='update'),

    # Ensure no spacing in between '<int:' and 'dog_id>/'
    path('delete/<int:dog_id>/', views.delete, name='delete'),
]
