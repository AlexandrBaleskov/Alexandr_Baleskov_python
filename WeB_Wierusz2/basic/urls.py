from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.news, name = "home"),
    path('aboute',views.aboute, name = "aboute"),
    path('personnel',views.personnel, name = "personnel"),
    path('SMB', views.SMB , name = "SMB"),
    path('SMB_OK', views.SMB_Ok , name = "SMB_Ok"),
    path('info', views.info , name = "info"),
    path('contacts', views.contacts , name = "contacts"),
    
]
if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




















