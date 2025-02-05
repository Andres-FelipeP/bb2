
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='HomePage'),
    path('ContactMe', views.contactMe, name='contactMe'),
    path('AboutMe', views.aboutMe, name='AboutMe'),
    path('Services', views.catalog, name='Catalog'),
    path('Service/<int:product_id>/', views.product, name='Product'),

]


