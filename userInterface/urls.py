from django.urls import path
from .views import index
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import path, include,  re_path


app_name = 'userInterface'
urlpatterns = [
    path('', index, name = ''),
    path('join', index),
    path('create', index),
    path('room/<str:roomCode>', index)

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print(static("static/", document_root=settings.STATIC_ROOT))