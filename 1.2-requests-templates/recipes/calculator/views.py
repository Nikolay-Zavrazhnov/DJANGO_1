
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
'patatos': {
        'картофель, гр': 500,
        'масло, гр': 50,
        'соль, гр': 15,

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

def dish_views(request, dish):

    persons = int(request.GET.get("servings", 2))
    new_dict = {}

    for ingredient, vol in DATA[dish].items():
        new_dict[ingredient] = round(vol * persons, 2)

    context = {
            'recipe': {
                dish: new_dict
              }
        }
    template_name = 'calculator/index.html'
    return render(request, template_name, context)




