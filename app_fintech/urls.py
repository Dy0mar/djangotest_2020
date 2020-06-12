"""blogify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('', views.transaction_list_view, name='transaction-list'),
    path('transaction/create', views.transaction_create, name='transaction-create'),
    path('transaction/<int:pk>', views.transaction_detail, name='transaction-detail'),
    path('transaction/edit/<int:pk>', views.transaction_update, name='transaction-update'),
    path('transaction/delete/<int:pk>', views.transaction_delete, name='transaction-delete'),

    path('statuses', views.status_list_view, name='status-list'),
    path('status/create', views.status_create, name='status-create'),
    path('status/<int:pk>', views.status_detail, name='status-detail'),
    path('status/edit/<int:pk>', views.status_update, name='status-update'),
    path('status/delete/<int:pk>', views.status_delete, name='status-delete'),

    # url(r'^post/update/(?P<pk>\d+)/$', update_post, name='update-post'),
    # url(r'^post/delete/(?P<pk>\d+)/$', delete_post, name='delete-post'),
    # url(r'^post/(?P<pk>\d+)/$', post_detail, name='post-detail'),
    # url(r'^$', author_blog_list, name='author-blog-list'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
