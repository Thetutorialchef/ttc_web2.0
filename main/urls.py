from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="index"),
    path("view/", views.view, name="view"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
