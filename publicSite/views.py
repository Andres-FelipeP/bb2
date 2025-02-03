from django.shortcuts import render
from main.models import Category, Products, AboutMePage, HomeContent, PinkyBeautyBarSalonImages, PhotoGallery, SocialMedia, Values, Certificates, ServicesPage, PinkyBeautyBarSalonImages, PinkyBeautyBarInfo,VideoGallery, Benefits, Myths, Recommendations, Process
from django.shortcuts import get_object_or_404



def home(request):
    home_content = HomeContent.objects.first()
    salon_images = PinkyBeautyBarSalonImages.objects.all()
    products_info = PhotoGallery.objects.all().order_by('order')[:7]
    social_media = SocialMedia.objects.first()
    pinky_beauty_bar_info = PinkyBeautyBarInfo.objects.first()
    categories = Category.objects.all()

    admin = "AdminUser.objects.get(username="")"
    admin_wpp = "f'{admin.country_code}{admin.phone_number}'"
    admin_address = "admin.address"

    return render(request, 'homePage.html', {'home_content': home_content,'categories':categories, 'salon_images': salon_images, 'products_info': products_info, 'admin_wpp': admin_wpp, 'social_media':social_media, 'admin_address': admin_address, 'pinky_beauty_bar_info': pinky_beauty_bar_info})

def contactMe(request):
    return render(request, 'contactMe.html')


def aboutMe(request):
    about_me = AboutMePage.objects.first()
    values = Values.objects.all()
    certificates = Certificates.objects.all()
    products = Products.objects.all()

    return render(request, 'aboutPage.html', {'about_me': about_me, 'values': values, 'certificates': certificates, 'products_info':products})


def catalog(request):
    service = ServicesPage.objects.first()
    categories = Category.objects.all()
    selected_category = request.GET.get('category')

    if selected_category:
        products = Products.objects.filter(categories__id=selected_category).distinct()
    else:
        products = Products.objects.all()


    return render(request, 'catalogPage.html', {'products': products, 'service': service, 'categories':categories, 'selected_category':selected_category})



def product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    social_media = SocialMedia.objects.first()
    benefits = Benefits.objects.filter(product=product)
    process = Process.objects.filter(product=product)
    myths = Myths.objects.filter(product=product)
    recommendations = Recommendations.objects.filter(product=product)
    photo_gallery = PhotoGallery.objects.filter(product=product).order_by('order')
    video_gallery = VideoGallery.objects.filter(product=product).order_by('order')


    return render(request, 'productPage.html', {'social_media':social_media,'product': product, 'benefits':benefits, 'process':process, 'myths':myths, 'recommendations': recommendations, 'photo_gallery': photo_gallery, 'video_gallery': video_gallery})


