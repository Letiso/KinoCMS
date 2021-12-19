from django.urls import path
from . import views

urlpatterns = [
    path('', views.statistics, name="statistics"),

    path('banners', views.BannersView.as_view(), name="banners"),
    path('movies', views.MoviesView.as_view(), name="movies"),
    path('movie_card/<str:pk>', views.MovieCardView.as_view(), name="movie_card"),

    path('cinemas', views.cinemas, name="cinemas_conf"),

    path('news', views.NewsView.as_view(), name="news_conf"),
    path('news_card/<str:pk>', views.NewsCardView.as_view(), name="news_card"),
    path('news_card/<int:pk>/delete', views.NewsCardDeleteView.as_view(), name="delete_news"),

    path('promotion', views.PromotionListView.as_view(), name="promotion_conf"),
    path('promotion_card/<str:pk>', views.PromotionCardView.as_view(), name="promotion_card"),
    path('promotion_card/<int:pk>/delete', views.PromotionCardDeleteView.as_view(), name="delete_promotion"),

    path('pages', views.pages, name="pages"),

    path('users', views.UsersView.as_view(), name="users"),
    path('user/<int:pk>/update', views.UserUpdateView.as_view(), name="update_user"),
    path('user/<int:pk>/delete', views.UserDeleteView.as_view(), name="delete_user"),

    path('mailing', views.mailing, name="mailing"),
    ]
