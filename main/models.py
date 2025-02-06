from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date, timezone
from django.dispatch import receiver
import os
from django.db.models.signals import post_delete, pre_save


class PinkyBeautyBarInfo(models.Model):
    address = models.TextField(null=True, blank=True)
    country_code = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    logo = models.ImageField(upload_to='PinkyBeautyBarInfo/', default="default/img.png")
    instagram = models.URLField(max_length=200, blank=True, null=True)
    address_url = models.URLField(null=True, blank=True)



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


# Función auxiliar para evitar borrar imágenes dentro de "default/"
def is_default_image(file_path):
    return file_path and "default/" in file_path  # Asegúrate de que la carpeta es "default/" y no "defaults/"

def delete_file(instance, file_field):
    """Elimina el archivo si no está en la carpeta default/."""
    file = getattr(instance, file_field)
    if file and not is_default_image(file.name):
        file.delete(save=False)

def delete_old_file(instance, file_field, model_class):
    """Elimina el archivo antiguo si cambia y no está en default/."""
    if instance.pk:
        try:
            old_instance = model_class.objects.get(pk=instance.pk)
            old_file = getattr(old_instance, file_field)
            new_file = getattr(instance, file_field)
            if old_file and old_file != new_file and not is_default_image(old_file.name):
                old_file.delete(save=False)
        except model_class.DoesNotExist:
            pass


@receiver(post_delete, sender=Products)
def delete_products_files(sender, instance, **kwargs):
    delete_file(instance, "banner")
    delete_file(instance, "image1")
    delete_file(instance, "image2")
    delete_file(instance, "image3")

@receiver(pre_save, sender=Products)
def delete_old_products_files(sender, instance, **kwargs):
    delete_old_file(instance, "banner", Products)
    delete_old_file(instance, "image1", Products)
    delete_old_file(instance, "image2", Products)
    delete_old_file(instance, "image3", Products)

@receiver(post_delete, sender=VideoGallery)
def delete_videogallery_files(sender, instance, **kwargs):
    delete_file(instance, "video_file")

@receiver(pre_save, sender=VideoGallery)
def delete_old_videogallery_files(sender, instance, **kwargs):
    delete_old_file(instance, "video_file", VideoGallery)

@receiver(post_delete, sender=HomeContent)
def delete_homecontent_files(sender, instance, **kwargs):
    delete_file(instance, "banner")
    delete_file(instance, "image1")
    delete_file(instance, "image2")
    delete_file(instance, "image3")
    delete_file(instance, "image4")

@receiver(pre_save, sender=HomeContent)
def delete_old_homecontent_files(sender, instance, **kwargs):
    delete_old_file(instance, "banner", HomeContent)
    delete_old_file(instance, "image1", HomeContent)
    delete_old_file(instance, "image2", HomeContent)
    delete_old_file(instance, "image3", HomeContent)
    delete_old_file(instance, "image4", HomeContent)

@receiver(post_delete, sender=PinkyBeautyBarSalonImages)
def delete_pinky_images(sender, instance, **kwargs):
    delete_file(instance, "image")

@receiver(pre_save, sender=PinkyBeautyBarSalonImages)
def delete_old_pinky_images(sender, instance, **kwargs):
    delete_old_file(instance, "image", PinkyBeautyBarSalonImages)


@receiver(post_delete, sender=AboutMePage)
def delete_aboutme_files(sender, instance, **kwargs):
    delete_file(instance, "banner")
    delete_file(instance, "image1")
    delete_file(instance, "image2")

@receiver(pre_save, sender=AboutMePage)
def delete_old_aboutme_files(sender, instance, **kwargs):
    delete_old_file(instance, "banner", AboutMePage)
    delete_old_file(instance, "image1", AboutMePage)
    delete_old_file(instance, "image2", AboutMePage)

@receiver(post_delete, sender=ServicesPage)
def delete_servicespage_files(sender, instance, **kwargs):
    delete_file(instance, "banner")

@receiver(pre_save, sender=ServicesPage)
def delete_old_servicespage_files(sender, instance, **kwargs):
    delete_old_file(instance, "banner", ServicesPage)

@receiver(post_delete, sender=PhotoGallery)
def delete_photogallery_files(sender, instance, **kwargs):
    delete_file(instance, "image")

@receiver(pre_save, sender=PhotoGallery)
def delete_old_photogallery_files(sender, instance, **kwargs):
    delete_old_file(instance, "image", PhotoGallery)