from django.http import HttpResponse
from django.utils import timezone
from .models import RequestLog
from django.views.decorators.csrf import csrf_exempt

from .generate_video.aaa import running_text

def log_request(func):
    def wrapper(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        RequestLog.objects.create(
            path=request.path,
            method=request.method,
            timestamp=timezone.now()
        )
        return response
    return wrapper

# Создаём функцию для ответа сервера
@csrf_exempt
@log_request
def index(request):
    """Получает текст из запроса, обращается к файлу, который создаёт и сохраняет видео.
    Возвращает видео как response"""
    text = request.GET.get('text', '')
    video = running_text(text)
    with open('/content/testproject/polls/running_text.avi', 'rb') as f:
        response = HttpResponse(f, content_type='video/avi')  # Создаем HTTPResponse с видеофайлом
        response['Content-Disposition'] = f'attachment; filename="{text}.avi"'  # Устанавливаем имя файла для скачивания
    return response


#def index(request):
    
    # get from requests.params | kwargs - your text
    # push this text to cv2 create video
    # push this video to HttpResponse 
#    return HttpResponse("Hello, world. You're at the polls index.")
