from django.contrib import admin
from .models import Category,HomeContent,AboutMePage,ServicesPage,Benefits,Process,Myths,Recommendations,PhotoGallery,VideoGallery,PinkyBeautyBarSalonImages,Products,Certificates, PinkyBeautyBarInfo, PinkyBeautyBarSalonImages, Values

admin.site.register(PinkyBeautyBarInfo)
admin.site.register(HomeContent)
admin.site.register(PinkyBeautyBarSalonImages)
admin.site.register(AboutMePage)
admin.site.register(Values)
admin.site.register(Certificates)
admin.site.register(ServicesPage)
admin.site.register(Products)
admin.site.register(Benefits)
admin.site.register(Process)
admin.site.register(Myths)
admin.site.register(Recommendations)
admin.site.register(PhotoGallery)
admin.site.register(VideoGallery)
admin.site.register(Category)

