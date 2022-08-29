
from django.http import HttpResponse
from django.shortcuts import render, reverse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def omlet_views(request):
    vol_pers = int(request.GET.get("servings", 1))
    context = {
      'recipe': {
          'omlet': {
              'яйца, шт': 2 * vol_pers,
        'молоко, л': 0.1 * vol_pers,
        'соль, ч.л.': 0.5 * vol_pers,
          }
      }
    }
    template_name = 'calculator/index.html'
    return render(request, template_name, context)

def pasta_views(request):
    vol_pers = int(request.GET.get("servings", 1))
    context = {
      'recipe': {
          'pasta': {
        'макароны, г': 0.3 * vol_pers,
        'сыр, г': 0.05 * vol_pers,
        }
      }
    }
    template_name = 'calculator/index.html'
    return render(request, template_name, context)

def buter_views(request):
    vol_pers = int(request.GET.get("servings", 1))
    context = {
      'recipe': {
          'buter': {
        'хлеб, ломтик': 1 * vol_pers,
        'колбаса, ломтик': 1 * vol_pers,
        'сыр, ломтик': 1 * vol_pers,
        'помидор, ломтик': 1 * vol_pers,
          }
      }
    }
    template_name = 'calculator/index.html'
    return render(request, template_name, context)



