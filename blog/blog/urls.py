from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from post.views import LandingPage
from post.views import PostDetail

from . import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LandingPage.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
