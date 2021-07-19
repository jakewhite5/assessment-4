from django.http.response import HttpResponse
from django.shortcuts import render
from craigslistjr.models import Category, Post



def index(request):
    return HttpResponse("index")

def list_categories(request):
    data = {
        'categories' : Category.objects.all()
    }
    return render(request, 'categories/category_details.html', data)

def category_new(request):
    return HttpResponse("category new")

def category_details(request, category_id):
    return HttpResponse("category details")

def category_edit(request, category_id):
    return HttpResponse("category edit")

def category_delete(request, category_id):
    return HttpResponse("category delete")

#posts

def post_new(request, category_id):
    return HttpResponse("post new")

def post_details(request, category_id, post_id):
    return HttpResponse("home page")

def post_edit(request, category_id, post_id):
    return HttpResponse("post edit")

def post_delete(request, category_id, post_id):
    return HttpResponse("home page")


