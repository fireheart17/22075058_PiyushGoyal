from django.urls import path,include
from .views import home,createShortURL,redirect,fetch_created_urls
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',home,name = 'home'),
    path('create/',createShortURL,name='create'),
    path('<str:url>',redirect,name = 'redirect'), 
    path('createdUrls/',fetch_created_urls,name='fetcjurls')
]
# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)
