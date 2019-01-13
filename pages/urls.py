from django.urls import path
from. import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),  
    path('contact/', views.contact, name="contact"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"), 
    path('register/', views.register_user, name="register"), 
    path('edit_profile/', views.edit_profile, name="edit_profile"), 
    path('change_password/', views.change_password, name="change_password"), 
    path('delete/<list_id>', views.delete, name="delete"),
    path('cross_off/<list_id>', views.cross_off, name="cross_off"),
    path('uncross/<list_id>', views.uncross, name="uncross"),
    path('edit_list/<list_id>', views.edit_list, name="edit_list"),
    path('addressbook/', views.addressbook, name="addressbook"), 
    path('add_address/', views.add_address, name="add_address"), 


]