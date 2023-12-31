"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from blog import views

from django.conf import settings
from django.conf.urls.static import static

from shop import webhooks

urlpatterns = i18n_patterns(
    path("", views.post_list, name='home'),
    path("admin/", admin.site.urls),
    path("account/", include('account.urls')),
    path("blog/", include('blog.urls')),
    path("shop/", include('shop.urls')),
    path('rosetta/', include('rosetta.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Callback URL 국제화 예외 처리
urlpatterns += [
    path('webhook/toss/', webhooks.toss_webhook, name='toss-webhook'),
    path('social-auth/', include('social_django.urls', namespace='social')),
]
