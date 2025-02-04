from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date, timezone
from django.dispatch import receiver
import os
from django.db.models.signals import post_delete, pre_save


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


@receiver(post_delete, sender=Products)
def delete_product_files(sender, instance, **kwargs):
    """Elimina las imágenes del producto al eliminarlo."""
    if instance.banner:
        instance.banner.delete(save=False)
    if instance.image1:
        instance.image1.delete(save=False)
    if instance.image2:
        instance.image2.delete(save=False)
    if instance.image3:
        instance.image3.delete(save=False)


@receiver(post_delete, sender=VideoGallery)
def delete_video_files(sender, instance, **kwargs):
    """Elimina el video cuando se borra la galería."""
    if instance.video_file:
        instance.video_file.delete(save=False)

@receiver(post_delete, sender=HomeContent)
def delete_homecontent_files(sender, instance, **kwargs):
    """Elimina imágenes cuando se borra una instancia de HomeContent."""
    if instance.banner:
        instance.banner.delete(save=False)
    if instance.image1:
        instance.image1.delete(save=False)
    if instance.image2:
        instance.image2.delete(save=False)
    if instance.image3:
        instance.image3.delete(save=False)
    if instance.image4:
        instance.image4.delete(save=False)

@receiver(post_delete, sender=PinkyBeautyBarSalonImages)
def delete_pinky_images(sender, instance, **kwargs):
    """Elimina la imagen cuando se borra una instancia de PinkyBeautyBarSalonImages."""
    if instance.image:
        instance.image.delete(save=False)

@receiver(post_delete, sender=AboutMePage)
def delete_aboutme_files(sender, instance, **kwargs):
    """Elimina imágenes cuando se borra una instancia de AboutMePage."""
    if instance.banner:
        instance.banner.delete(save=False)
    if instance.image1:
        instance.image1.delete(save=False)
    if instance.image2:
        instance.image2.delete(save=False)

@receiver(post_delete, sender=ServicesPage)
def delete_servicespage_files(sender, instance, **kwargs):
    """Elimina el banner cuando se borra una instancia de ServicesPage."""
    if instance.banner:
        instance.banner.delete(save=False)

@receiver(post_delete, sender=PhotoGallery)
def delete_photogallery_files(sender, instance, **kwargs):
    """Elimina la imagen cuando se borra una instancia de PhotoGallery."""
    if instance.image:
        instance.image.delete(save=False)


# 🔄 Eliminar archivos antiguos cuando se actualiza una instancia
@receiver(pre_save, sender=HomeContent)
def delete_old_homecontent_files(sender, instance, **kwargs):
    """Elimina imágenes anteriores cuando se actualiza una instancia de HomeContent."""
    if instance.pk:
        try:
            old_instance = HomeContent.objects.get(pk=instance.pk)
            if old_instance.banner and old_instance.banner != instance.banner:
                old_instance.banner.delete(save=False)
            if old_instance.image1 and old_instance.image1 != instance.image1:
                old_instance.image1.delete(save=False)
            if old_instance.image2 and old_instance.image2 != instance.image2:
                old_instance.image2.delete(save=False)
            if old_instance.image3 and old_instance.image3 != instance.image3:
                old_instance.image3.delete(save=False)
            if old_instance.image4 and old_instance.image4 != instance.image4:
                old_instance.image4.delete(save=False)
        except HomeContent.DoesNotExist:
            pass

@receiver(pre_save, sender=PinkyBeautyBarSalonImages)
def delete_old_pinky_images(sender, instance, **kwargs):
    """Elimina la imagen anterior cuando se actualiza una instancia de PinkyBeautyBarSalonImages."""
    if instance.pk:
        try:
            old_instance = PinkyBeautyBarSalonImages.objects.get(pk=instance.pk)
            if old_instance.image and old_instance.image != instance.image:
                old_instance.image.delete(save=False)
        except PinkyBeautyBarSalonImages.DoesNotExist:
            pass

@receiver(pre_save, sender=AboutMePage)
def delete_old_aboutme_files(sender, instance, **kwargs):
    """Elimina imágenes anteriores cuando se actualiza una instancia de AboutMePage."""
    if instance.pk:
        try:
            old_instance = AboutMePage.objects.get(pk=instance.pk)
            if old_instance.banner and old_instance.banner != instance.banner:
                old_instance.banner.delete(save=False)
            if old_instance.image1 and old_instance.image1 != instance.image1:
                old_instance.image1.delete(save=False)
            if old_instance.image2 and old_instance.image2 != instance.image2:
                old_instance.image2.delete(save=False)
        except AboutMePage.DoesNotExist:
            pass

@receiver(pre_save, sender=ServicesPage)
def delete_old_servicespage_files(sender, instance, **kwargs):
    """Elimina el banner anterior cuando se actualiza una instancia de ServicesPage."""
    if instance.pk:
        try:
            old_instance = ServicesPage.objects.get(pk=instance.pk)
            if old_instance.banner and old_instance.banner != instance.banner:
                old_instance.banner.delete(save=False)
        except ServicesPage.DoesNotExist:
            pass

@receiver(pre_save, sender=PhotoGallery)
def delete_old_photogallery_files(sender, instance, **kwargs):
    """Elimina la imagen anterior cuando se actualiza una instancia de PhotoGallery."""
    if instance.pk:
        try:
            old_instance = PhotoGallery.objects.get(pk=instance.pk)
            if old_instance.image and old_instance.image != instance.image:
                old_instance.image.delete(save=False)
        except PhotoGallery.DoesNotExist:
            pass

@receiver(pre_save, sender=Products)
def delete_old_product_files(sender, instance, **kwargs):
    """Elimina las imágenes anteriores cuando se actualiza."""
    if instance.pk:
        try:
            old_instance = Products.objects.get(pk=instance.pk)
            if old_instance.banner and old_instance.banner != instance.banner:
                old_instance.banner.delete(save=False)
            if old_instance.image1 and old_instance.image1 != instance.image1:
                old_instance.image1.delete(save=False)
            if old_instance.image2 and old_instance.image2 != instance.image2:
                old_instance.image2.delete(save=False)
            if old_instance.image3 and old_instance.image3 != instance.image3:
                old_instance.image3.delete(save=False)
        except Products.DoesNotExist:
            pass

@receiver(pre_save, sender=VideoGallery)
def delete_old_video_files(sender, instance, **kwargs):
    """Elimina el video anterior cuando se actualiza."""
    if instance.pk:
        try:
            old_instance = VideoGallery.objects.get(pk=instance.pk)
            if old_instance.video_file and old_instance.video_file != instance.video_file:
                old_instance.video_file.delete(save=False)
        except VideoGallery.DoesNotExist:
            pass