from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome),
    path('test/', views.ors_test),
    path('welcome/', views.welcome),
    path('signup/', views.user_signup),
    path('signin/', views.user_signin),
    path('logout/', views.user_logout),
    path('list/', views.user_list),
    path('save/', views.user_save),
    path('save/<int:id>/', views.user_save),
    path('delete/<int:id>/', views.delete_user)
]
