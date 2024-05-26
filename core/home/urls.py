from django.contrib import admin
from django.urls import include, path
from .views import *

urlpatterns = [
    path('eiin', store_eiin),
    path('eiins/', home, name='home'), # List all EIIN entries
    path('eiins/store/', store_eiin, name='store_eiin'), # Create a new EIIN entry
    path('eiins/<int:pk>/', get_eiin, name='get_eiin'), # Retrieve a single EIIN entry by ID
    path('eiins/<int:pk>/update/',update_eiin, name='update_eiin'), # Update a single EIIN entry by ID
    path('eiins/<int:pk>/delete/',delete_eiin, name='delete_eiin'), # Delete a single EIIN entry by ID
]