from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from website import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ImageCaption.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index', views.index),
    url(r'^upload', views.uploadImg),
    url(r'^show', views.showImg),
    url(r'^caption', views.caption),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
