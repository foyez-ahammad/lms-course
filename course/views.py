from django.shortcuts import render, redirect
from .models import *

# course filter
from django.template.loader import render_to_string
from django.http import JsonResponse

# total duration sum
from django.db.models import Sum


def home(request):
    course_menu_category = Categories.get_all_category(Categories)
    # category = Categories.objects.all().order_by('id')[0:5]
    category = Categories.objects.all().order_by('id')
    courses = Course.objects.filter(status='PUBLISH').order_by('-id')
    context = {
        'course_menu_category': course_menu_category,
        'category': category,
        'course': courses,
    }
    return render(request, 'main/home.html', context)


def contact(request):
    course_menu_category = Categories.get_all_category(Categories)
    context = {
        'course_menu_category': course_menu_category,
    }
    return render(request, 'main/contact.html', context)


def about(request):
    course_menu_category = Categories.get_all_category(Categories)
    context = {
        'course_menu_category': course_menu_category,
    }
    return render(request, 'main/about.html', context)


def course(request):
    category = Categories.get_all_category(Categories)
    course_menu_category = Categories.get_all_category(Categories)
    level = Level.objects.all()
    course = Course.objects.all()
    author = Author.objects.all()

    context = {
        'course_menu_category': course_menu_category,
        'category': category,
        'level': level,
        'course': course,
        'author': author,
    }
    return render(request, 'main/course.html', context)


def course_filter(request):
    course_menu_category = Categories.get_all_category(Categories)
    categories = request.GET.getlist('category[]')
    author = request.GET.getlist('author[]')
    level = request.GET.getlist('level[]')

    if categories:
        course = Course.objects.filter(
            category__id__in=categories).order_by('-id')
    elif author:
        course = Author.objects.filter(author__id__in=author).order_by('-id')
    elif level:
        course = Course.objects.filter(level__id__in=level).order_by('-id')
    else:
        course = Course.objects.all().order_by('-id')

    context = {
        'course_menu_category': course_menu_category,
        'course': course,
    }

    t = render_to_string('course/course_filter.html', context)

    return JsonResponse({'data': t})


def course_detail(request, slug):
    course_menu_category = Categories.get_all_category(Categories)
    duration = Video.objects.filter(course__slug=slug).aggregate(sum=Sum('duration'))

    course = Course.objects.filter(slug=slug)

    if course.exists():
        course = course.first()
    else:
        return redirect('404')
    context = {
        'course_menu_category': course_menu_category,
        'course': course,
        'duration': duration,
    }
    return render(request, 'course/course_detail.html', context)


def search(request):
    course_menu_category = Categories.get_all_category(Categories)
    query = request.GET['query']
    course = Course.objects.filter(title__icontains=query)
    context = {
        'course_menu_category': course_menu_category,
        'course': course,
    }
    return render(request, 'course/search.html', context)


def page_not_found(request):
    course_menu_category = Categories.get_all_category(Categories)
    context = {
        'course_menu_category': course_menu_category,
    }
    return render(request, 'erorr/404.html', context)

def course_watch(request, slug):
    course_menu_category = Categories.get_all_category(Categories)
    duration = Video.objects.filter(course__slug=slug).aggregate(sum=Sum('duration'))
    lecture = request.GET.get('lecture')
    video = Video.objects.get(id= lecture)

    course = Course.objects.filter(slug=slug)

    if course.exists():
        course = course.first()
    else:
        return redirect('404')
    context = {
        'course_menu_category': course_menu_category,
        'course': course,
        'duration': duration,
        'video': video
    }
    return render(request, 'course/course_watch.html', context)