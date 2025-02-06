from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import HomeContent, AboutMePage, Certificates, Products, ServicesPage, Benefits, Process, \
    Myths, Recommendations, PhotoGallery, VideoGallery, PinkyBeautyBarSalonImages, Values, PinkyBeautyBarInfo, Category


class PinkyBeautyBarInfoForms(forms.ModelForm):
    class Meta:
        model = PinkyBeautyBarInfo
        fields = ['address', 'country_code', 'phone_number', 'logo', 'instagram', 'address_url']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-10'}),
            'country_code': forms.NumberInput(attrs={'class': 'form-control bg-danger bg-opacity-10'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-10'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control bg-danger bg-opacity-10'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control bg-danger bg-opacity-10'}),
            'address_url': forms.URLInput(attrs={'class': 'form-control bg-danger bg-opacity-10'}),

        }



class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-25'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control bg-danger bg-opacity-25'}))



class HomeContentForm(forms.ModelForm):
    class Meta:
        model = HomeContent
        fields = ['slogan', 'banner', 'who_am_i', 'skills', 'image1', 'image2', 'image3', 'image4', 'home_mission', 'home_vision', 'attitude']
        widgets = {
            'slogan': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-10', 'name': 'slogan'}),
            'banner': forms.ClearableFileInput(attrs={'class': 'form-control  ', 'name': 'banner'}),
            'who_am_i': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-10 ', 'name': 'who_am_i'}),
            'skills': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-10 ', 'name': 'skills'}),
            'image1': forms.ClearableFileInput(attrs={'class': 'form-control  ', 'name': 'image1'}),
            'image2': forms.ClearableFileInput(attrs={'class': 'form-control  ', 'name': 'image2'}),
            'image3': forms.ClearableFileInput(attrs={'class': 'form-control ', 'name': 'image3'}),
            'image4': forms.ClearableFileInput(attrs={'class': 'form-control  ', 'name': 'image4'}),
            'home_mission': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-10 ', 'name': 'home_mission'}),
            'home_vision': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-10 ', 'name': 'home_vision'}),
            'attitude': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-10 ', 'name': 'attitude'}),

        }


class AboutMePageForm(forms.ModelForm):
    class Meta:
        model = AboutMePage
        fields = ['banner', 'description', 'image1', 'image2', 'about_me_mission', 'about_me_vision', 'competence']
        widgets = {
            'banner': forms.ClearableFileInput(attrs={'class': 'form-control ', 'name': 'banner'}),
            'description': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-10', 'name': 'description'}),
            'competence': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-10', 'name': 'about_me_competence'}),
            'about_me_mission': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-10', 'name': 'about_me_mission'}),
            'about_me_vision': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-10', 'name': 'about_me_vision'}),
            'image1': forms.ClearableFileInput(attrs={'class': 'form-control', 'name': 'image1'}),
            'image2': forms.ClearableFileInput(attrs={'class': 'form-control', 'name': 'image2'}),
        }


class CertificatesForm(forms.ModelForm):
    class Meta:
        model = Certificates
        fields = ['tittle', 'description']
        widgets = {
            'tittle': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-25', 'name': 'certificates_tittle'}),
            'description': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-25', 'name': 'certificates_description'}),
        }

class ValuesForm(forms.ModelForm):
    class Meta:
        model = Values
        fields = ['tittle', 'description']
        widgets = {
            'tittle': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-25', 'name': 'values_tittle'}),
            'description': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-25', 'name': 'values_description'}),
        }

class ServicesPageForm(forms.ModelForm):
    class Meta:
        model = ServicesPage
        fields = ['banner']
        widgets = {
            'banner': forms.ClearableFileInput(attrs={'class': 'form-control', 'name': 'banner'}),
        }



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'})
        }


class ProductsForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    class Meta:
        model = Products
        fields = ['tittle', 'banner', 'subtittle', 'description', 'duration', 'price', 'image1', 'image2', 'image3', 'short_subtittle', 'categories']
        widgets = {
            'tittle': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-10'}),
            'banner': forms.ClearableFileInput(attrs={'class': 'form-control '}),
            'subtittle': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-10'}),
            'short_subtittle': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-10'}),
            'description': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-10'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control bg-danger bg-opacity-10'}),
            'price': forms.NumberInput(attrs={'class': 'form-control bg-danger bg-opacity-10'}),
            'image1': forms.ClearableFileInput(attrs={'class': 'form-control '}),
            'image2': forms.ClearableFileInput(attrs={'class': 'form-control '}),
            'image3': forms.ClearableFileInput(attrs={'class': 'form-control '}),

        }


class BenefitsForms(forms.ModelForm):
    class Meta:
        model = Benefits
        fields = ['tittle', 'description']
        widgets = {
            'tittle': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-25'}),
            'description': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-25'}),
        }


class ProcessForms(forms.ModelForm):
    class Meta:
        model = Process
        fields = ['tittle', 'description']
        widgets = {
            'tittle': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-25'}),
            'description': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-25'}),
        }



class MythsForms(forms.ModelForm):
    class Meta:
        model = Myths
        fields = ['tittle', 'description']
        widgets = {
            'tittle': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-25'}),
            'description': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-25'}),
        }


class RecommendationsForms(forms.ModelForm):
    class Meta:
        model = Recommendations
        fields = ['tittle', 'description']
        widgets = {
            'tittle': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-25'}),
            'description': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-25'}),
        }



class PhotoGalleryForm(forms.ModelForm):
    class Meta:
        model = PhotoGallery
        fields = ['order', 'image']
        widgets = {
            'order': forms.NumberInput(attrs={'class': 'form-control bg-danger bg-opacity-25'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control bg-danger bg-opacity-25'}),
        }


class VideoGalleryForm(forms.ModelForm):
    class Meta:
        model = VideoGallery
        fields = ['order', 'video_file', 'video_youtube_url']
        widgets = {
            'order': forms.NumberInput(attrs={'class': 'form-control bg-danger bg-opacity-25'}),
            'video_file': forms.ClearableFileInput(attrs={'class': 'form-control bg-danger bg-opacity-25'}),
            'video_youtube_url': forms.URLInput(attrs={'class': 'form-control bg-danger bg-opacity-25'}),
        }




class PinkyBeautyBarSalonImagesForm(forms.ModelForm):
    class Meta:
        model = PinkyBeautyBarSalonImages
        fields = ['tittle', 'description', 'image']
        widgets = {
            'tittle': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-25'}),
            'description': forms.TextInput(attrs={'class': 'form-control bg-danger bg-opacity-25'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control bg-danger bg-opacity-25'}),

        }
