from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("", views.index,name='home'),
    path("about", views.about,name='about'),
    path("contact", views.contact,name='contact'),
    path("whycps", views.whycps,name='whycps'),
    path("register_user", views.register_user,name='register_user'),
    path("offer_share", views.offer_share,name='offer_share'),
    path('logout', views.logoutuser,name="logout"),
    path('addnew', views.addnew,name="addnew"),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
   # path('delete/<int:id>', views.destroy),







]
