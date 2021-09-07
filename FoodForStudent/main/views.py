from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Recipe, Step, Ingredient, Category


#def index(request):
#    recipes = Recipe.objects.all()
#    return render(request, "main/index.html", {'recipes': recipes})

def recipe_list(request):
    object_list = Recipe.objects.all()

    paginator = Paginator(list(object_list), 2)  # 5 рецептов на каждой странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    try:
        Recipes = paginator.page(page_number)
    except PageNotAnInteger:
        Recipes = paginator.page(1)
    except EmptyPage:
        Recipes = paginator.page(paginator.num_pages)
    print(page_number)
    return render(request, 'main/index.html', {'page_obj': page_obj, 'recipes': Recipes})

def recipe_category(request, slug):
    category = {'meat':'Мясо',
                'bird':'Птица',
                'fish':'Рыба',
                'bakery':'Выпечка',
                'salat':'Салаты',
                'cereals':'Крупы',
                'vegetables':'Овощи',
                'cold':'Холодное',
                'sweet':'Сладкое'}
    this_category = category[slug]
    object_list = Recipe.objects.all().filter(category = Category.objects.get(name=this_category) )

    paginator = Paginator(list(object_list), 2)  # 5 рецептов на каждой странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    try:
        Recipes = paginator.page(page_number)
    except PageNotAnInteger:
        Recipes = paginator.page(1)
    except EmptyPage:
        Recipes = paginator.page(paginator.num_pages)
    print(page_number)
    return render(request, 'main/index.html', {'page_obj': page_obj, 'recipes': Recipes})

def recipe_detail(request, id):
    object = Recipe.objects.get(id=id)

    ingredients = Ingredient.objects.all().filter(recipe_id=id)

    steps = Step.objects.all().filter(recipe_id=id)

  # print(ing_list[0]['ing'])
    context = {'recipe': object,
               'ingredients': ingredients,
               'steps': steps}

    return render(request, 'main/recipe.html', context=context)