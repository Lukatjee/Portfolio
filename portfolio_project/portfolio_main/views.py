from django.shortcuts import render
from .models import Post, Intro


def portfolio(request):

    projects = Post.objects.all().filter(page='portfolio')
    intro = Intro.objects.all().filter(page='portfolio')

    context = {

        'projects': projects,
        'intro': intro

    }

    return render(request, 'portfolio.html', context)


def erasmus(request):

    post = Post.objects.all().filter(page='erasmus')
    intro = Intro.objects.all().filter(page='erasmus')

    context = {

        'erasmus': post,
        'intro': intro

    }

    return render(request, 'erasmus.html', context)
