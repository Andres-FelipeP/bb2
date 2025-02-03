from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date, timezone


class SocialMedia(models.Model):
    instagram = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Social Media"


class PinkyBeautyBarInfo(models.Model):
    address = models.TextField(null=True, blank=True)
    country_code = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)




class HomeContent(models.Model):
    slogan = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='home_images/')
    who_am_i = models.TextField()
    skills = models.TextField()
    image1 = models.ImageField(upload_to='home_images/', default="default/img.png")
    image2 = models.ImageField(upload_to='home_images/', default="default/img.png")
    image3 = models.ImageField(upload_to='home_images/', default="default/img.png")
    image4 = models.ImageField(upload_to='home_images/', default="default/img.png")
    home_mission = models.CharField(max_length=120)
    home_vision = models.CharField(max_length=120)
    attitude = models.CharField(max_length=120)

    def __str__(self):
        return "HomePage"


class PinkyBeautyBarSalonImages(models.Model):
    tittle = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pinky_beauty_bar_salon_images/', default="default/img.png")

    def __str__(self):
        return self.tittle


class AboutMePage(models.Model):
    banner = models.ImageField(upload_to='AboutMe/')
    description = models.TextField()
    competence = models.TextField()
    about_me_mission = models.TextField()
    about_me_vision = models.TextField()
    image1 = models.ImageField(upload_to='AboutMe/', default="default/img.png")
    image2 = models.ImageField(upload_to='AboutMe/', default="default/img.png")

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
    banner = models.ImageField(upload_to='ServicesPage/', default="default/img.png")
    def __str__(self):
        return "ServicesPage"

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    tittle = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='ProductsBanner/')
    subtittle = models.CharField(max_length=200)
    short_subtittle = models.CharField(max_length=100, default='My product')

    description = models.TextField()
    duration = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image1 = models.ImageField(upload_to='ProductsImage/', default="default/img.png")
    image2 = models.ImageField(upload_to='ProductsImage/', default="default/img.png")
    image3 = models.ImageField(upload_to='ProductsImage/', default="default/img.png")
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
    image = models.ImageField(upload_to='ProductsPhotoGallery/', default="default/img.png")
    order = models.IntegerField()


    def __str__(self):
        return f"Photo {self.order}"


class VideoGallery(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='video_gallery')
    video_file = models.FileField(upload_to='ProductsVideoGallery/', blank=True, null=True)
    video_youtube_url = models.URLField(max_length=200, blank=True, null=True)
    order = models.IntegerField()

    def __str__(self):
        return f"Video {self.order}"


