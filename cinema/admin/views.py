from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView, View
from django.contrib.auth import get_user_model
from .forms import ExtendedUserUpdateForm, BackgroundImageForm
from django.http import HttpResponseRedirect


def statistics(request):
    context = {
        'title': 'Статистика',
    }
    return render(request, 'admin/statistics.html', context)


# region Banners
class BannersView(View):

    def get(self, request):
        background_form = BackgroundImageForm(request.POST or None)

        context = {
            'forms': {
                # 'top_banner': TopBannerForm(),
                'background': background_form,
            }
        }

        return render(request, 'admin/banners/index.html', context)

    def post(self, request):
        background_form = BackgroundImageForm(request.POST, request.FILES)

        context = {
            'forms': {
                # 'top_banner': TopBannerForm(),
                'background': background_form,
            }
        }

        if background_form.is_valid():
            background_form.save()
            return HttpResponseRedirect('banners')

        return render(request, 'admin/banners/index.html', context)
# endregion Banners


def movies(request):
    context = {
        'title': 'Фильмы',
    }
    return render(request, 'admin/movies.html', context)


def cinemas(request):
    context = {
        'title': 'Кинотеатры',
    }
    return render(request, 'admin/cinemas.html', context)


def news(request):
    context = {
        'title': 'Новости',
    }
    return render(request, 'admin/news.html', context)


def promotion(request):
    context = {
        'title': 'Акции',
    }
    return render(request, 'admin/promotion.html', context)


def pages(request):
    context = {
        'title': 'Страницы',
    }
    return render(request, 'admin/pages.html', context)


# region User
def users(request):
    context = {
        'title': 'Пользователи',
        'fields': ['ID', 'Ред./Удал.', 'Логин', 'Email', 'Номер телефона',
                   'Имя', 'Фамилия', 'Пол', 'Язык', 'Дата рождения', 'Адрес', 'Был(а)',
                   'Регистрация', 'Сотрудник', 'Админ', ],
        'users': get_user_model().objects.all(),
    }

    return render(request, 'admin/users/users.html', context)


class UserUpdateView(UpdateView):
    model = get_user_model()
    success_url = '/admin/users'
    template_name = 'admin/users/update.html'

    form_class = ExtendedUserUpdateForm


class UserDeleteView(View):

    @staticmethod
    def get(request, pk):
        model = get_user_model()
        user_to_delete = get_object_or_404(model, pk=pk)
        user_to_delete.delete()
        return redirect('users')
# endregion User


def mailing(request):
    context = {
        'title': 'Рассылка',
    }
    return render(request, 'admin/mailing.html', context)
