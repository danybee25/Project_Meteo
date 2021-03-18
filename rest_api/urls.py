from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api_overview"),
    path('mountain-list/', views.mountain_list, name='mountain-list'),
    path('mountain-create/', views.create_mountain_data, name='mountain-create'),
    path('mountain/<str:pk>', views.per_mountain_data, name='mountain'),
    path('mountain-update/<str:pk>', views.update_mountain_data, name='mountain-update'),
    path('mountain-delete/<str:pk>', views.delete_mountain_data, name='mountain-delete'),
    path('mountain-search/<str:pk>', views.search_mountain_data, name='mountain-update')
]