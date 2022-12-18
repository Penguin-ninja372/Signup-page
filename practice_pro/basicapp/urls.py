from django.urls import path
from basicapp import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="index"),
    path("about/", views.AboutPage.as_view(), name="about"),
    path("form/", views.NewUserForm.as_view(), name="new_user"),
    path("users/", views.UserList.as_view(), name="user_list"),
]