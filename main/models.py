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
    video_file = CloudinaryField('video')
    video_youtube_url = models.URLField(max_length=200, blank=True, null=True)
    order = models.IntegerField()

    def __str__(self):
        return f"Video {self.order}"

def is_default_image(file_path):
    return file_path and "default_img" in file_path  # Verifica si la imagen es la predeterminada

def delete_file(file_path):
    """Elimina el archivo de Cloudinary."""
    if file_path and not is_default_image(file_path):  # Evita borrar imágenes predeterminadas
        public_id = file_path.split("/")[-1].split(".")[0]  # Obtén el public_id de Cloudinary
        cloudinary.uploader.destroy(public_id)

def delete_old_file(instance, file_field, model_class):
    """Elimina el archivo antiguo de Cloudinary si cambia."""
    if instance.pk:
        try:
            old_instance = model_class.objects.get(pk=instance.pk)
            old_file = getattr(old_instance, file_field)
            new_file = getattr(instance, file_field)
            if old_file and old_file != new_file and old_file.url and not is_default_image(old_file.url):
                public_id = old_file.url.split("/")[-1].split(".")[0]  # Obtén el public_id
                cloudinary.uploader.destroy(public_id)
        except model_class.DoesNotExist:
            pass


@receiver(post_delete, sender=Products)
def delete_products_files(sender, instance, **kwargs):
    delete_file(instance.banner.url)
    delete_file(instance.image1.url)
    delete_file(instance.image2.url)
    delete_file(instance.image3.url)

@receiver(pre_save, sender=Products)
def delete_old_products_files(sender, instance, **kwargs):
    delete_old_file(instance, "banner", Products)
    delete_old_file(instance, "image1", Products)
    delete_old_file(instance, "image2", Products)
    delete_old_file(instance, "image3", Products)

@receiver(post_delete, sender=VideoGallery)
def delete_videogallery_files(sender, instance, **kwargs):
    delete_file(instance.video_file)

@receiver(pre_save, sender=VideoGallery)
def delete_old_videogallery_files(sender, instance, **kwargs):
    delete_old_file(instance, "video_file", VideoGallery)

@receiver(post_delete, sender=HomeContent)
def delete_homecontent_files(sender, instance, **kwargs):
    delete_file(instance.banner.url)
    delete_file(instance.image1.url)
    delete_file(instance.image2.url)
    delete_file(instance.image3.url)
    delete_file(instance.image4.url)

@receiver(pre_save, sender=HomeContent)
def delete_old_homecontent_files(sender, instance, **kwargs):
    delete_old_file(instance, "banner", HomeContent)
    delete_old_file(instance, "image1", HomeContent)
    delete_old_file(instance, "image2", HomeContent)
    delete_old_file(instance, "image3", HomeContent)
    delete_old_file(instance, "image4", HomeContent)

@receiver(post_delete, sender=PinkyBeautyBarSalonImages)
def delete_pinky_images(sender, instance, **kwargs):
    delete_file(instance.image)

@receiver(pre_save, sender=PinkyBeautyBarSalonImages)
def delete_old_pinky_images(sender, instance, **kwargs):
    delete_old_file(instance, "image", PinkyBeautyBarSalonImages)


@receiver(post_delete, sender=AboutMePage)
def delete_aboutme_files(sender, instance, **kwargs):
    delete_file(instance.banner)
    delete_file(instance.image1)
    delete_file(instance.image2)

@receiver(pre_save, sender=AboutMePage)
def delete_old_aboutme_files(sender, instance, **kwargs):
    delete_old_file(instance, "banner", AboutMePage)
    delete_old_file(instance, "image1", AboutMePage)
    delete_old_file(instance, "image2", AboutMePage)

@receiver(post_delete, sender=ServicesPage)
def delete_servicespage_files(sender, instance, **kwargs):
    delete_file(instance.banner)

@receiver(pre_save, sender=ServicesPage)
def delete_old_servicespage_files(sender, instance, **kwargs):
    delete_old_file(instance, "banner", ServicesPage)

@receiver(post_delete, sender=PhotoGallery)
def delete_photogallery_files(sender, instance, **kwargs):
    delete_file(instance.image)

@receiver(pre_save, sender=PhotoGallery)
def delete_old_photogallery_files(sender, instance, **kwargs):
    delete_old_file(instance, "image", PhotoGallery)


