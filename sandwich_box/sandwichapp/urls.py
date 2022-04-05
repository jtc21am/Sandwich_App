from django.urls import path
from sandwichapp.views import SandwichappView, IngredientsListView, Sandwich_GeneratorView

urlpatterns = [
    # sandwich home
    path('', SandwichappView.as_view(), name='sandwich'),
    # sandwich/ingredients/<str:ingredient_type>
    path('ingredients/<str:ingredient_type>', IngredientsListView.as_view(), name = 'ingredients_list'),
    # sandwich/random
    path('random', Sandwich_GeneratorView.as_view(), name = 'sandwich_generator')
]