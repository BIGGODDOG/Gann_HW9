from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.template import loader
from .forms import AppReviewForm, BookReviewForm, PersonSearchForm
from django.core.paginator import Paginator

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render(request=request))


def app_review(request: HttpRequest):
    if request.method == 'POST':
        form = AppReviewForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            return render(request, 'app_review_result.html', context)
    else:
        form = AppReviewForm()
    return render(request, 'app_review.html', {'form': form})


def book_review(request: HttpRequest):
    if request.method == 'POST':
        form = BookReviewForm(request.POST)
        if form.is_valid():
            context = form.cleaned_data
            return render(request, 'book_review_result.html', context)
    else:
        form = BookReviewForm()
    return render(request, 'book_review.html', {'form': form})


def search_person(request: HttpRequest):
    form = PersonSearchForm(request.GET or None)
    results = []
    if form.is_valid():
        full_name = form.cleaned_data['full_name']
        city = form.cleaned_data['city']
        results = get_person_data(full_name, city)  
    paginator = Paginator(results, 10)  # Пагинация по 10 элементов
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'search_person.html', {'form': form, 'page_obj': page_obj})

def get_person_data(full_name, city):
    # Заглушка
    return [{'name': f'{full_name} {i}', 'city': city, 'info': 'Пример информации'} for i in range(50)]
