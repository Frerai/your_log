"""learning_log URL Configuration

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
from django.urls import path, include

urlpatterns = [
    # all the URLs that can be requested from the admin site
    path('admin/', admin.site.urls),
    # included the files "urls.py" from the project app/project folder "users" - this will include any URL that starts with "users"
    path('users/', include('users.urls')),
    # included URLs to the module "learning_log"
    path('', include('learning_logs.urls')),
]
