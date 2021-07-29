from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from craigslistjr.models import Category, Post
from craigslistjr.forms import CategoryForm, PostForm



def index(request):
    return render(request, 'home.html')

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
            return redirect("craig:category_detail", category_id=category.id)
        except:
            return HttpResponse("Error updating category")
    data = {
        "create_or_update": False,
        "form": form
    }
    return render(request, "categories/category_form.html", data)

def category_delete(request, category_id):
    if request.method == "GET":
        category = Category.objects.get(id=category_id)
        category.delete()
        return redirect('craig:category_list')
    else:
        return HttpResponse('something broke')
#posts
def get_post(post_id):
    return Post.objects.get(id=post_id)

def post_new(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return HttpResponse("That post no longer exists")
    form = PostForm(request.POST or None, initial={'category':category})
    if request.method == "POST":
        try:
            form.save()
            return redirect("craig:category_detail", category_id)
        except:
            return HttpResponse("Error adding new post")
    data = {
        "create_or_update": True,
        "form": form
    }
    return render(request, "posts/post_form.html", data)

def post_details(request, category_id, post_id):

    try:
        post =  Post.objects.get(pk=post_id)
    except:
        print('error')
        return HttpResponse("That post doesn't exist somehow")
    
    data = {
        'post':post
    }
    return render(request, 'posts/post_details.html', data)

def post_edit(request, post_id, category_id):

    try:
        post =  Post.objects.get(pk=post_id)
    except:
        print('error')
        return HttpResponse("That post doesn't exist somehow?")

    form = PostForm(request.POST or None, instance=post)

    if request.method == "POST":
        try:
            form.save()
            return redirect("craig:post_details", post_id=post_id, category_id=post.category.id)
        except:
            return HttpResponse("Error updating post")
    data = {
        "create_or_update": False,
        "form": form
    }
    return render(request, "posts/post_form.html", data)

    

def post_delete(request, category_id, post_id):
    if request.method == "GET":
        post = get_post(post_id)
        print(post)
        post.delete()
    return redirect('craig:category_detail', category_id=category_id)

