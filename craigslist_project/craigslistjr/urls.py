from django.urls import path, include
from craigslistjr import views

app_name ="craig"

urlpatterns = [
    path('', views.index, name="home"),
    path("categories", views.list_categories, name="category_list"), # A page listing all the categories
    path("categories/new", views.category_new, name="category_new"), # A page with a form to create a new category
    path("categories/<int:category_id>", views.category_details, name='category_detail'), # A page to view the detail of a specific category and a list of all of its associated posts
    path("categories/<int:category_id>/edit", views.category_edit, name='category_edit'), # A page with a form to update a specific category, with current values filled in already. Also include the ability to delete the specific category here.
    path("categories/<int:category_id>/delete", views.category_delete, name='category_delete'), # A page with a form to update a specific category, with current values filled in already. Also include the ability to delete the specific category here. 
    path("categories/<int:category_id>/posts/new", views.post_new, name='post_new'), #A page with a form to create a new post, under the current category by default.
    path("categories/<int:category_id>/posts/<int:post_id>", views.post_details, name='post_details'), #A page to view the detail of a specific post. Also include the ability go back to the parent category detail page
    path("categories/<int:category_id>/posts/<int:post_id>/edit", views.post_edit, name='post_edit'), #A page with a form to update a specific post, with current values filled in already. Also include the ability to delete the specific post here.
    path("categories/<int:category_id>/posts/<int:post_id>/delete", views.post_delete, name='post_delete') #A page with a form to update a specific post, with current values filled in already. Also include the ability to delete the specific post here.
]
