from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date, timezone
from django.dispatch import receiver
import os
from django.db.models.signals import post_delete, pre_save
from cloudinary.models import CloudinaryField
import cloudinary.uploader


class PinkyBeautyBarInfo(models.Model):
    address = models.TextField(null=True, blank=True)
    country_code = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    logo = CloudinaryField('image', default='default_img')
    instagram = models.URLField(max_length=200, blank=True, null=True)
    address_url = models.URLField(null=True, blank=True)



class HomeContent(models.Model):
    slogan = models.CharField(max_length=200)
    banner = CloudinaryField('image', default='default_img')
    who_am_i = models.TextField()
    skills = models.TextField()
    image1 = CloudinaryField('image', default='default_img')
    image2 = CloudinaryField('image', default='default_img')
    image3 = CloudinaryField('image', default='default_img')
    image4 = CloudinaryField('image', default='default_img')
    home_mission = models.CharField(max_length=120)
    home_vision = models.CharField(max_length=120)
    attitude = models.CharField(max_length=120)

    def __str__(self):
        return "HomePage"


class PinkyBeautyBarSalonImages(models.Model):
    tittle = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = CloudinaryField('image', default='default_img')

    def __str__(self):
        return self.tittle


class AboutMePage(models.Model):
    banner = CloudinaryField('image', default='default_img')
    description = models.TextField()
    competence = models.TextField()
    about_me_mission = models.TextField()
    about_me_vision = models.TextField()
    image1 = CloudinaryField('image', default='default_img')
    image2 = CloudinaryField('image', default='default_img')

    def __str__(self):
        return "AboutMePage"


class Values(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.tittle


class Certificates(models.Model):
    tittle = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.tittle


class ServicesPage(models.Model):
    banner = CloudinaryField('image', default='default_img')
    def __str__(self):
        return "ServicesPage"


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    tittle = models.CharField(max_length=200)
    banner = CloudinaryField('image', default='default_img')
    subtittle = models.CharField(max_length=200)
    short_subtittle = models.CharField(max_length=100, default='My product')
    description = models.TextField()
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image1 = CloudinaryField('image', default='default_img')
    image2 = CloudinaryField('image', default='default_img')
    image3 = CloudinaryField('image', default='default_img')
    categories = models.ManyToManyField(Category, related_name="products")


    def __str__(self):
        return self.tittle


class Benefits(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='benefits')
    tittle = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.tittle


class Process(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='process')
    tittle = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.tittle


class Myths(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='myths')
    tittle = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.tittle


class Recommendations(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='recommendations')
    tittle = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.tittle


class PhotoGallery(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='photo_gallery')
    image = CloudinaryField('image', default='default_img')
    order = models.IntegerField()

    def __str__(self):
        return f"Photo {self.order}"


class VideoGallery(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='video_gallery')
    video_file = CloudinaryField('video', resource_type='video')  # <-- Aquí indicamos que es un video
    video_youtube_url = models.URLField(max_length=200, blank=True, null=True)
    order = models.IntegerField()

    def __str__(self):
        return f"Video {self.order}"

