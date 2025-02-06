from .models import PinkyBeautyBarInfo

def pinky_beauty_bar_info(request):
    return {
        'pinky_beauty_bar_info': PinkyBeautyBarInfo.objects.first()
    }