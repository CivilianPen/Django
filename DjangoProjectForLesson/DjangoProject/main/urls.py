from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.main, name = "main"),
    path('python', views.page),
    path('javascript', views.page2),
    path('python/<int:post_id>/', views.PostF, name="python"),
    path('javascript/<int:post_id>/',views.PostF2,name = 'javascript'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)