from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.admin_logout, name='logout'),

    path('dashboard/editHomePage', views.edit_home, name='edit_home'),
    path('dashboard/editAboutMe', views.edit_about_me, name='edit_about_me'),
    path('dashboard/editServices', views.edit_services, name='edit_services'),

    path('dashboard/editMyProfile', views.edit_my_profile, name='edit_my_profile'),

    path('dashboard/myProducts/categories', views.category_list, name='list_category'),
    path('dashboard/myProducts/categories/create', views.create_category, name='create_category'),

    path('dashboard/myProducts/categories/<int:category_id>/', views.category_products, name='category_products'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),

    path('dashboard/myProducts/products/create/', views.create_product, name='create_product'),
    path('dashboard/myProducts/<int:product_id>/products/delete/', views.delete_product, name='delete_product'),

    path('dashboard/myProducts/edit/<int:pk>/', views.edit_product, name='edit_product'),



    path('dashboard/myProducts/benefits/add/<int:product_id>', views.add_benefit, name='add_benefit'),
    path('dashboard/myProducts/benefits/edit/<int:benefit_id>/', views.edit_benefit, name='edit_benefit'),
    path('dashboard/myProducts/benefits/delete/<int:benefit_id>/', views.delete_benefit, name='delete_benefit'),

    path('dashboard/myProducts/process/add<int:product_id>/', views.add_process, name='add_process'),
    path('dashboard/myProducts/process/edit/<int:process_id>/', views.edit_process, name='edit_process'),
    path('dashboard/myProducts/process/delete/<int:process_id>/', views.delete_process, name='delete_process'),


    path('dashboard/myProducts/myths/add/<int:product_id>/', views.add_Myths, name='add_myths'),
    path('dashboard/myProducts/myths/edit/<int:Myth_id>/', views.edit_Myth, name='edit_myths'),
    path('dashboard/myProducts/myths/delete/<int:Myth_id>/', views.delete_Myth, name='delete_myths'),


    path('dashboard/myProducts/recommendations/add/<int:product_id>/', views.add_recommendations, name='add_recommendations'),
    path('dashboard/myProducts/recommendations/edit/<int:recommendations_id>/', views.edit_recommendations, name='edit_recommendations'),
    path('dashboard/myProducts/recommendations/delete/<int:recommendations_id>/', views.delete_recommendations, name='delete_recommendations'),


    path('dashboard/myProducts/photos/add/<int:product_id>/', views.add_photo, name='add_photo'),
    path('dashboard/myProducts/photos/edit/<int:photo_id>/', views.edit_photo, name='edit_photo'),
    path('dashboard/myProducts/photos/delete/<int:photo_id>/', views.delete_photo, name='delete_photo'),


    path('dashboard/myProducts/video/add/<int:product_id>/', views.add_video, name='add_video'),
    path('dashboard/myProducts/video/edit/<int:video_id>/', views.edit_video, name='edit_video'),
    path('dashboard/myProducts/video/delete/<int:video_id>/', views.delete_video, name='delete_video'),


    path('dashboard/editAboutMe/values/add/', views.add_values, name='add_values'),
    path('dashboard/editAboutMe/values/edit/<int:value_id>/', views.edit_values, name='edit_values'),
    path('dashboard/editAboutMe/values/delete/<int:value_id>/', views.delete_values, name='delete_values'),



    path('dashboard/editAboutMe/certificates/add/', views.add_certificates, name='add_certificates'),
    path('dashboard/editAboutMe/certificates/edit/<int:certificate_id>/', views.edit_certificates, name='edit_certificates'),
    path('dashboard/editAboutMe/certificates/delete/<int:certificate_id>/', views.delete_certificates, name='delete_certificates'),

    path('dashboard/editBeautySalonImages/', views.edit_beauty_salon_images, name='edit_salon'),
    path('dashboard/editBeautySalonImages/add', views.add_beauty_salon_images, name='add_salon_images'),
    path('dashboard/editBeautySalonImages/delete/<int:image_id>/', views.delete_beauty_salon_images, name='delete_salon_images'),
    path('dashboard/editBeautySalonImages/edit/<int:image_id>/', views.edit_beauty_salon_images_2,name='edit_salon_images'),


]
