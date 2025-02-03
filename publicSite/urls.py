
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='HomePage'),
    path('Contact Me', views.contactMe, name='contactMe'),
    path('About Me', views.aboutMe, name='AboutMe'),
    path('Services', views.catalog, name='Catalog'),
    path('Service/<int:product_id>/', views.product, name='Product'),

]


