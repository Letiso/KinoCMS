from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name="login"),
    path('logout', views.LogoutView.as_view(next_page='/'), name="logout"),
    path('signup', views.SignUpView.as_view(), name="signup"),
    path('update_account', views.SignUpView.as_view(), name="update_account"),
    path('delete_account', views.SignUpView.as_view(), name="delete_account"),
    path('account', views.user_account, name="account"),
]
