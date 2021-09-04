from django.db import models


class Category(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=50)
    image = models.ImageField(default='/static/main/img/recipe/depositphotos_269592716-stock-photo-thumbnail-images-placeholder-forums-blogs.jpg')
    text = models.TextField()
    time = models.CharField(max_length=50, default='10 минут')
    difficult_l = models.CharField(max_length=50, default='Легко')
    data = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Step(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    number = models.IntegerField()
    image = models.ImageField(default='/static/main/img/recipe/depositphotos_269592716-stock-photo-thumbnail-images-placeholder-forums-blogs.jpg')
    text = models.TextField()

    def __str__(self):

        return str(self.number) + ' шаг' + ' рецепта ' + str(self.recipe_id)

class Ingredient(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    title = models.CharField(default='',max_length=50)
    amount = models.CharField(default='',max_length=20)

