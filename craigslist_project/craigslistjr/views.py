from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from craigslistjr.models import Category, Post
from craigslistjr.forms import CategoryForm, PostForm



def index(request):
    return HttpResponse("index")

def list_categories(request):
    data = {
        'categories' : Category.objects.all()
    }
    return render(request, 'categories/category_list.html', data)

def category_new(request):
    form = CategoryForm(request.POST or None)

    if request.method == "POST":
        try:
            form.save()
            return redirect("craig:category_list")
        except:
            return HttpResponse("Error creating category")
    data = {
        "create_or_update": True,
        "form": form
    }
    return render(request, 'categories/category_form.html', data)

def category_details(request, category_id):
    try: 
        category =  Category.objects.get(pk=category_id)
    except:
        print('error')
        return HttpResponse("That category doesn't exist somehow")
    data = {
        'category' : category
    }
    return render(request, 'categories/category_details.html', data)

def category_edit(request, category_id):

    try:
        category =  Category.objects.get(pk=category_id)
    except:
        print('error')
        return HttpResponse("That category doesn't exist somehow")

    form = CategoryForm(request.POST or None, instance=category)

    if request.method == "POST":
        try:
            form.save()
            return redirect("craig:category_detail", category_id=category_id)
        except:
            return HttpResponse("Error updating category")
    data = {
        "create_or_update": False,
        "form": form
    }
    return render(request, "categories/category_form.html", data)

def category_delete(request, category_id):
    return HttpResponse("category delete")

#posts

def post_new(request, post_id):
    form = PostForm(request.POST or None)

    if request.method == "POST":
        try:
            form.save()
            return redirect("craig:category_list")
        except:
            print('error')
            return HttpResponse("Error creating post")
    data = {
        "posts": Post.objects.filter(post=post_id),
        "form": form
    }
    return render(request, 'posts/post_list.html', data)

def post_details(request, post_id):

    try:
        post =  Post.objects.get(pk=post_id)
    except:
        print('error')
        return HttpResponse("That post doesn't exist somehow")
    
    data = {
        'post':post
    }
    return render(request, 'posts/post_details.html', data)

def post_edit(request, category_id, post_id):
    return HttpResponse("post edit")

def post_delete(request, category_id, post_id):
    return HttpResponse("home page")


