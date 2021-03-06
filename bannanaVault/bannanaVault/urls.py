"""bannanaVault URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from graphene_django.views import GraphQLView
from django.contrib import admin
from django.urls import path
from users.views import login_view, home, signup, logout_view
from passwords.views import delete_password_entry

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', GraphQLView.as_view(graphiql=True)),
    path('', home, name='home'),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path('signup', signup, name="signup"),
    path('delete/<int:pk>/', delete_password_entry, name="delete-password"),
]
