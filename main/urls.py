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
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("privacy-policy/", views.policy, name="privacy-policy"),
    path("disclaimer/", views.disclaimer, name="disclaimer"),
    path("contribute/", views.contribute, name="contribute"),
    path("tutorials/", views.tutorials, name="tutorials"),
    path("sitemap/", views.sitemap, name="sitemap"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
