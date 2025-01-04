from django.shortcuts import render


def index(request):
    header =  "User's data"
    langs = ['Python', 'CSS', 'JS']
    user = {'name': 'Nikita', 'age': 26}
    address = ('Фронтовиков', '8/3', 633)

    data = {'header': header, 'langs': langs, 'user': user, 'address': address}
    return render(request, 'hot/index.html', context=data)
