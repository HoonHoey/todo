from django.shortcuts import render
from .models import Favorite, Todo
# Create your views here.
def index(request):
    return render(request, "second/index.html")

def favorite(request):
    data = Favorite.objects.all()
    return render(request, "second/favorite.html",
        {'datas':data}
    )
def todo(request):
    data = Todo.objects
    if 'group' in request.GET:
        data = data.filter(group__name=request.GET['group'])
    if 'end_date' in request.GET:
        data = data.filter(end_date__gte=request.GET['end_date'])
    return render(request, "second/todo.html",
        {'datas':data.all()}
    )

def favorite_detail(request, seq):
    detail = Favorite.objects.get(pk=seq)
    return render(request, "second/favorite_detail.html",{
        'detail' : detail
    })
    
    
    