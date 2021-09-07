from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('category/<slug:slug>/', views.recipe_category, name='recipe_category' ),
    path('details/<int:id>/', views.recipe_detail, name='recipe_detail' )
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)