from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.MainPageView.as_view(), name="main_page"),

    path('poster', views.MoviesPosterView.as_view(), name="poster"),
    path('poster/movie_card', views.MovieCardView.as_view(), name="movie_card"),

    path('soon', views.MoviesSoonView.as_view(), name="soon"),

    path('timetable', views.MovieSessionsTimetableView.as_view(), name="timetable"),
    path('timetable/ticket_booking', views.TicketBookingView.as_view(), name="ticket_booking"),

    path('cinemas', views.CinemasView.as_view(), name="cinemas"),
    path('cinemas/cinema_card', views.cinema_card, name="cinema_card"),
    path('cinemas/hall_card', views.hall_card, name="hall_card"),

    path('promotion', views.promotion, name="promotion"),
    path('promotion/promotion_card', views.promotion_card, name="promotion_card"),

    path('about_the_cinema', views.about_the_cinema, name="about_the_cinema"),
    path('about_the_cinema/advertising', views.advertising, name="advertising"),
    path('about_the_cinema/cafe_bar', views.cafe_bar, name="cafe_bar"),
    path('about_the_cinema/child_room', views.child_room, name="child_room"),
    path('about_the_cinema/contacts', views.contacts, name="contacts"),
    path('about_the_cinema/mobile_applications', views.mobile_applications, name="mobile_applications"),
    path('about_the_cinema/news', views.news, name="news"),
    path('about_the_cinema/vip_hall', views.vip_hall, name="vip_hall"),
    ]
