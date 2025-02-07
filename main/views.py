from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import PinkyBeautyBarSalonImagesForm, ServicesPageForm, ValuesForm, CertificatesForm, AboutMePageForm, \
    HomeContentForm, ProductsForm, Benefits, Process, Myths, Recommendations, \
    BenefitsForms, ProcessForms, MythsForms, RecommendationsForms, PhotoGalleryForm, VideoGalleryForm, \
    PinkyBeautyBarInfoForms, CategoryForm
from .models import Certificates, Values, HomeContent, Products, PhotoGallery, VideoGallery, \
    PinkyBeautyBarSalonImages, AboutMePage, ServicesPage, PinkyBeautyBarInfo, Category
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.forms import modelformset_factory
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirigir si ya está logueado

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})



@login_required
def dashboard(request):
    return render(request, 'dashboard.html', )


def admin_logout(request):
    logout(request)
    return redirect('login')

import cloudinary

@login_required
def edit_home(request):
    home_content, created = HomeContent.objects.get_or_create(
        defaults={
            "slogan": "Slogan",
            "banner": "default/img.png",
            "who_am_i": "who am i?",
            "skills": "skills",
            "image1": "https://res.cloudinary.com/df8ssknyd/image/upload/v1738909522/istockphoto-1354776457-612x612_erjftg.jpg",
            "image2": "default/img.png",
            "image3": "default/img.png",
            "image4": "default/img.png",
            "home_mission": "home mission",
            "home_vision": "home vision",
            "attitude": "attitude",

        }
    )
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    print(cloudinary.config().cloud_name)  # Debería imprimir tu Cloud Name
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

    salon_images = PinkyBeautyBarSalonImages.objects.all()
    products_info = Products.objects.all()[:7]

    pinky_beauty_bar_info, created = PinkyBeautyBarInfo.objects.get_or_create(
        defaults={
            'address': "1060 Plaza Dr kissimmee fl 34743",
            'country_code': "1",
            'phone_number': "000 0000 0000",
            'logo': "https://res.cloudinary.com/df8ssknyd/image/upload/v1738909522/istockphoto-1354776457-612x612_erjftg.jpg",
            'instagram': 'https://www.instagram.com/pinky.beauty.bar/',
            'address_url': 'https://maps.app.goo.gl/vdj2Qj8oC1tehJiL7'
        })

    categories = Category.objects.all()

    if request.method == "POST":
        form = HomeContentForm(request.POST, request.FILES, instance=home_content)
        if form.is_valid():
            form.save()
            return redirect('edit_home')
    else:
        form = HomeContentForm(instance=home_content)

    return render(request, 'edit_content_live_home_page.html', {'home_content': home_content, 'salon_images': salon_images, 'products_info': products_info, 'form': form, 'pinky_beauty_bar_info': pinky_beauty_bar_info, 'categories': categories})


@login_required
def edit_services(request):
    service, created = ServicesPage.objects.get_or_create(
        defaults={
            'banner': "default/img.png"
        })

    categories = Category.objects.all()

    products = Products.objects.all()

    if request.method == 'POST':
        service_form = ServicesPageForm(request.POST, request.FILES, instance=service)
        if service_form.is_valid():
            service_form.save()
            return redirect('edit_services')
    else:
        service_form = ServicesPageForm(instance=service)

    return render(request, 'edit_content_live_services.html', {'categories': categories, 'service': service, 'service_form': service_form, 'products': products})


@login_required
def edit_contact_me(request):
    return render(request, 'edit_content_live_contact_me.html', )


@login_required
def edit_my_profile(request):
    instance, created = PinkyBeautyBarInfo.objects.get_or_create(
        defaults={
            'address': "1060 Plaza Dr kissimmee fl 34743",
            'country_code': "1",
            'phone_number': "000 0000 0000",
            'logo': "https://res.cloudinary.com/df8ssknyd/image/upload/v1738909522/istockphoto-1354776457-612x612_erjftg.jpg",
            'instagram': 'https://www.instagram.com/pinky.beauty.bar/',
            'address_url': 'https://maps.app.goo.gl/vdj2Qj8oC1tehJiL7'

        })

    if request.method == "POST":
        form = PinkyBeautyBarInfoForms(request.POST, request.FILES, instance=instance)

        if form.is_valid():
            form.save()
            return redirect('edit_my_profile')  # Redirige para actualizar la vista con los nuevos datos

    else:
        form = PinkyBeautyBarInfoForms(instance=instance)


    return render(request, 'edit_content_live_my_profile.html', {'form': form, 'pinky_beauty_bar_info': instance})


@login_required
def category_list(request):
    products = Products.objects.all()
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories, 'products': products})


@login_required
def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'category_products.html', {'category': category, 'products': products})


@login_required
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoría creada exitosamente.")
            return redirect('list_category')  # Redirige a la lista de categorías
    else:
        form = CategoryForm()

    return render(request, 'create_category.html', {'form': form})


@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if category.products.exists():  # Si hay productos asociados, no permite eliminar
        messages.error(request, "No puedes eliminar esta categoría porque tiene productos asociados.")
    else:
        category.delete()
        messages.success(request, "Categoría eliminada exitosamente.")

    return redirect('list_category')


@login_required
def create_product(request):
    categories = Category.objects.all()

    if request.method == "POST":
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_category')  # Ajusta esta redirección a donde desees
    else:
        form = ProductsForm()
    return render(request, 'create_product.html', {'form': form, 'categories': categories})


@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect('list_category')  # Ajusta la redirección a donde desees
    return render(request, 'delete_product.html', {'product': product})



@login_required
def edit_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    benefits = Benefits.objects.filter(product=product)
    process = Process.objects.filter(product=product)
    myths = Myths.objects.filter(product=product)
    recommendations = Recommendations.objects.filter(product=product)
    photo_gallery = PhotoGallery.objects.filter(product=product).order_by('order')
    video_gallery = VideoGallery.objects.filter(product=product).order_by('order')

    if request.method == "POST":
        product_form = ProductsForm(request.POST, request.FILES, instance=product)

        if product_form.is_valid():
            product_form.save()
            return redirect('edit_product', product.id)


    else:
        product_form = ProductsForm(instance=product)

    return render(request, 'edit_product.html', {
        'product_form': product_form,
        'product': product,
        'benefits': benefits,
        'process': process,
        'myths': myths,
        'recommendations': recommendations,
        'photo_gallery': photo_gallery,
        'video_gallery': video_gallery,
    })


@login_required
def edit_about_me(request):
    about_me, created = AboutMePage.objects.get_or_create(
        defaults={
            "banner": "https://res.cloudinary.com/df8ssknyd/image/upload/v1738909522/istockphoto-1354776457-612x612_erjftg.jpg",
            "description": "description",
            "competence": "competence",
            "about_me_mission": "about_me_mission",
            "about_me_vision": "about_me_vision",
            "image1": "https://res.cloudinary.com/df8ssknyd/image/upload/v1738909522/istockphoto-1354776457-612x612_erjftg.jpg",
            "image2": "https://res.cloudinary.com/df8ssknyd/image/upload/v1738909522/istockphoto-1354776457-612x612_erjftg.jpg",
        }
    )

    values = Values.objects.all()
    certificates = Certificates.objects.all()
    products = Products.objects.all()

    if request.method == "POST":
        about_me_form = AboutMePageForm(request.POST, request.FILES, instance=about_me)
        if about_me_form.is_valid():
            about_me_form.save()
            return redirect('edit_about_me')

    else:
        about_me_form = AboutMePageForm(instance=about_me)

    return render(request, 'edit_content_live_about_me.html', {'about_me_form': about_me_form,
                                                                'about_me': about_me,
                                                                'values': values,
                                                                'certificates': certificates,
                                                                'products': products})

#About Me
#Values
@login_required
def add_values(request):
    if request.method == "POST":
        form = ValuesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edit_about_me')
    else:
        form = ValuesForm()
    return render(request, 'add_values.html', {'form': form})

@login_required
def edit_values(request, value_id):
    value = get_object_or_404(Values, id=value_id)
    if request.method == "POST":
        value.tittle = request.POST.get(f'values_tittle_{value_id}')
        value.description = request.POST.get(f'values_description_{value_id}')
        value.save()

        form = ValuesForm(request.POST, instance=value)
        if form.is_valid():
            form.save()
            return redirect('edit_about_me')

    else:
        form = ValuesForm(instance=value)

    return redirect('edit_about_me')


@login_required
def delete_values(request, value_id):
    value = get_object_or_404(Values, id=value_id)
    value.delete()
    return redirect('edit_about_me')

# Certificates
@login_required
def add_certificates(request):
    if request.method == "POST":
        form = CertificatesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edit_about_me')
    else:
        form = CertificatesForm()
    return render(request, 'add_certificates.html', {'form': form})


@login_required
def edit_certificates(request, certificate_id):
    certificate = get_object_or_404(Certificates, id=certificate_id)
    if request.method == "POST":
        certificate.tittle = request.POST.get(f'certificates_tittle_{certificate_id}')
        certificate.description = request.POST.get(f'certificates_description_{certificate_id}')
        certificate.save()

        form = CertificatesForm(request.POST, instance=certificate)
        if form.is_valid():
            form.save()
            return redirect('edit_about_me')

    else:
        form = CertificatesForm(instance=certificate)

    return redirect('edit_about_me')


@login_required
def delete_certificates(request, certificate_id):
    certificates = get_object_or_404(Certificates, id=certificate_id)
    certificates.delete()
    return redirect('edit_about_me')



# Benefit
@login_required
def add_benefit(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.method == "POST":
        form = BenefitsForms(request.POST)
        if form.is_valid():
            benefit = form.save(commit=False)
            benefit.product = product
            benefit.save()
            return redirect('edit_product', pk=product_id)
    else:
        form = BenefitsForms()
    return render(request, 'add_benefit.html', {'form': form, 'product': product})


@login_required
def edit_benefit(request, benefit_id):
    benefit = get_object_or_404(Benefits, id=benefit_id)
    if request.method == "POST":
        benefit.tittle = request.POST.get(f'benefits_tittle_{ benefit_id }')
        benefit.description = request.POST.get(f'benefits_description_{ benefit_id }')
        benefit.save()

        form = BenefitsForms(request.POST, instance=benefit)
        if form.is_valid():
            form.save()
            return redirect('edit_product', pk=benefit.product.id)
    else:
        form = BenefitsForms(instance=benefit)

    return redirect('edit_product', pk=benefit.product.id)


@login_required
def delete_benefit(request, benefit_id):
    benefit = get_object_or_404(Benefits, id=benefit_id)
    product_id = benefit.product.id
    benefit.delete()
    return redirect('edit_product', pk=product_id)


# ProcessForms
@login_required
def add_process(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.method == "POST":
        form = ProcessForms(request.POST)
        if form.is_valid():
            process = form.save(commit=False)
            process.product = product
            process.save()
            return redirect('edit_product', pk=product_id)
    else:
        form = ProcessForms()
    return render(request, 'add_process.html', {'form': form, 'product': product})


@login_required
def edit_process(request, process_id):
    process = get_object_or_404(Process, id=process_id)
    if request.method == "POST":
        process.tittle = request.POST.get(f'process_tittle_{process_id}')
        process.description = request.POST.get(f'process_description_{process_id}')
        process.save()

        form = ProcessForms(request.POST, instance=process)
        if form.is_valid():
            form.save()
            return redirect('edit_product', pk=process.product.id)
    else:
        form = ProcessForms(instance=process)
    return redirect('edit_product', pk=process.product.id)


@login_required
def delete_process(request, process_id):
    process = get_object_or_404(Process, id=process_id)
    product_id = process.product.id
    process.delete()
    return redirect('edit_product', pk=product_id)


# Myths
@login_required
def add_Myths(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.method == "POST":
        form = MythsForms(request.POST)
        if form.is_valid():
            myth = form.save(commit=False)
            myth.product = product
            myth.save()
            return redirect('edit_product', pk=product_id)
    else:
        form = MythsForms()
    return render(request, 'add_Myth.html', {'form': form, 'product': product})


@login_required
def edit_Myth(request, Myth_id):
    myth = get_object_or_404(Myths, id=Myth_id)
    if request.method == "POST":
        myth.tittle = request.POST.get(f'myths_tittle_{Myth_id}')
        myth.description = request.POST.get(f'myths_description_{Myth_id}')
        myth.save()

        form = MythsForms(request.POST, instance=myth)
        if form.is_valid():
            form.save()
            return redirect('edit_product', pk=myth.product.id)
    else:
        form = MythsForms(instance=myth)
    return redirect('edit_product', pk=myth.product.id)


@login_required
def delete_Myth(request, Myth_id):
    myth = get_object_or_404(Myths, id=Myth_id)
    product_id = myth.product.id
    myth.delete()
    return redirect('edit_product', pk=product_id)


# Recommendations
@login_required
def add_recommendations(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.method == "POST":
        form = RecommendationsForms(request.POST)
        if form.is_valid():
            recommendations = form.save(commit=False)
            recommendations.product = product
            recommendations.save()
            return redirect('edit_product', pk=product_id)
    else:
        form = RecommendationsForms()
    return render(request, 'add_recommendations.html', {'form': form, 'product': product})


@login_required
def edit_recommendations(request, recommendations_id):
    recommendations = get_object_or_404(Recommendations, id=recommendations_id)
    if request.method == "POST":
        recommendations.tittle = request.POST.get(f'recommendations_tittle_{recommendations_id}')
        recommendations.description = request.POST.get(f'recommendations_description_{recommendations_id}')
        recommendations.save()

        form = RecommendationsForms(request.POST, instance=recommendations)
        if form.is_valid():
            form.save()
            return redirect('edit_product', pk=recommendations.product.id)
    else:
        form = RecommendationsForms(instance=recommendations)
    return redirect('edit_product', pk=recommendations.product.id)


@login_required
def delete_recommendations(request, recommendations_id):
    recommendations = get_object_or_404(Recommendations, id=recommendations_id)
    product_id = recommendations.product.id
    recommendations.delete()
    return redirect('edit_product', pk=product_id)


# Photos
@login_required
def add_photo(request, product_id):
    product = get_object_or_404(Products, id=product_id)

    if request.method == "POST":
        form = PhotoGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.product = product
            photo.save()
            return redirect('edit_product', pk=product.id)
    else:
        form = PhotoGalleryForm()

    return render(request, 'add_photo.html', {'form': form, 'product': product})


@login_required
def edit_photo(request, photo_id):
    photo = get_object_or_404(PhotoGallery, id=photo_id)

    if request.method == "POST":
        form = PhotoGalleryForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('edit_product', pk=photo.product.id)
        else:
            print(form.errors)
    return redirect('edit_product', pk=photo.product.id)


@login_required
def delete_photo(request, photo_id):
    photo = get_object_or_404(PhotoGallery, id=photo_id)
    product_id = photo.product.id
    photo.delete()
    return redirect('edit_product', pk=product_id)


#Videos
@login_required
def add_video(request, product_id):
    product = get_object_or_404(Products, id=product_id)

    if request.method == "POST":
        form = VideoGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.product = product
            video.save()
            return redirect('edit_product', pk=product.id)
    else:
        form = VideoGalleryForm()

    return render(request, 'add_video.html', {'form': form, 'product': product})


@login_required
def edit_video(request, video_id):
    video = get_object_or_404(VideoGallery, id=video_id)

    if request.method == "POST":
        form = VideoGalleryForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('edit_product', pk=video.product.id)
        else:
            print(form.errors)

    return redirect('edit_product', pk=video.product.id)


@login_required
def delete_video(request, video_id):
    video = get_object_or_404(VideoGallery, id=video_id)
    product_id = video.product.id
    video.delete()
    return redirect('edit_product', pk=product_id)


@login_required
def edit_beauty_salon_images(request):
    salon_images = PinkyBeautyBarSalonImages.objects.all()

    return render(request, 'edit_beauty_salon_images.html', {'salon_images': salon_images})


@login_required
def add_beauty_salon_images(request):
    if request.method == "POST":
        form = PinkyBeautyBarSalonImagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('edit_salon')
    else:
        form = PinkyBeautyBarSalonImagesForm()

    return render(request,'add_beauty_salon_image.html', {'form': form})

@login_required
def edit_beauty_salon_images_2(request, image_id):
    photo = get_object_or_404(PinkyBeautyBarSalonImages, id=image_id)
    if request.method == "POST":
        form = PinkyBeautyBarSalonImagesForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('edit_salon')

    return redirect('edit_salon')

@login_required
def delete_beauty_salon_images(request, image_id):
    photo = get_object_or_404(PinkyBeautyBarSalonImages, id=image_id)
    photo.delete()
    return redirect('edit_salon')
