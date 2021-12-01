from django.shortcuts import render
from .models import TopBanner, BackgroundImage, NewsBanner


def index(request):
    context = {
            'top_banners': {
                'banners': TopBanner.objects.all(),
                'active_slide': TopBanner.objects.first(),
                'data_interval': '2500',
            },

            'background_image': {
                'banner': BackgroundImage.objects.first(),
            },

            'news_banners': {
                'banners': NewsBanner.objects.all(),
                'active_slide': NewsBanner.objects.first()
            },
    }
    return render(request, 'main/index.html', context)


def poster(request):
    return render(request, 'main/poster/poster.html')


def movie_card(request):
    return render(request, 'main/poster/movie_card.html')


def soon(request):
    return render(request, 'main/soon.html')


def timetable(request):
    return render(request, 'main/timetable/timetable.html')


def ticket_booking(request):
    return render(request, 'main/timetable/ticket_booking.html')


def cinemas(request):
    return render(request, 'main/cinemas/cinemas.html')


def cinema_card(request):
    return render(request, 'main/cinemas/cinema_card.html')


def hall_card(request):
    return render(request, 'main/cinemas/hall_card.html')


def promotion(request):
    return render(request, 'main/promotion/promotion.html')


def promotion_card(request):
    return render(request, 'main/promotion/promotion_card.html')


def about_the_cinema(request):
    return render(request, 'main/about_the_cinema/about_the_cinema.html')


def advertising(request):
    return render(request, 'main/about_the_cinema/advertising.html')


def cafe_bar(request):
    return render(request, 'main/about_the_cinema/cafe_bar.html')


def child_room(request):
    return render(request, 'main/about_the_cinema/child_room.html')


def contacts(request):
    return render(request, 'main/about_the_cinema/contacts.html')


def mobile_applications(request):
    return render(request, 'main/about_the_cinema/mobile_applications.html')


def news(request):
    return render(request, 'main/about_the_cinema/news.html')


def vip_hall(request):
    return render(request, 'main/about_the_cinema/vip_hall.html')


def user_account(request):
    return render(request, 'main/user_account.html')
