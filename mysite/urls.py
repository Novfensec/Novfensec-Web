"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from newsite.sitemaps import StaticViewSitemap,BlogViewSitemap
from django.contrib.sitemaps.views import sitemap

admin.site.site_header="Novfensec Inc."
admin.site.site_title="Novfensec Inc"
admin.site.index_title="Site Administration"

handler404='newsite.views.errora'
handler403='newsite.views.errorc'
handler400='newsite.views.errorb'
handler500='newsite.views.errord'

sitemaps={
    'sitemapview':StaticViewSitemap,
    'blogsitemapview':BlogViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('sitemap_index.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('', include('newsite.urls')),
    path('courses/', include('courses.urls')),
    path('blog/', include('blog.urls')),
    path('users/', include('users.urls')),
    path('projects/', include('projects.urls'))
]
