from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name="post", on_delete=models.CASCADE)

    def __str__(self):
        return f"model: {self.title}, {self.category}"
    

