"""django_freeshelf URL Configuration

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
from django.conf import settings
from django.urls import path
from django.urls import include
from books import views as book_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", book_views.homepage, name="homepage"),
    path("books/", book_views.list_books, name="list_books"),
    path("books/add", book_views.add_book, name="add_book"),
    path("books/<int:pk>", book_views.show_book, name="show_book"),
    path("books/<int:pk>/edit", book_views.edit_book, name="edit_book"),
    path("books/<int:pk>/delete", book_views.delete_book, name="delete_book"),
    path("accounts/", include('registration.backends.simple.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
