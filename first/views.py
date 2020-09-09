from django.shortcuts import render
from django.http import HttpResponse
from .models import Studendts
from .models import scores

# Create your views here.
def index(request):
    return render(request, 'first/index.html')

def students(request):

    students = Studendts.objects.all()
    print(students) 
    """
        SELECT *
            FROM studendts
    """
    return render(request, 'first/students.html', {
        'text':'안녕하세요',
        'students' : students
    })

def score(request):
    
    scores2 = scores.objects.all()
    print(scores2) 
    """
        SELECT *
            FROM scores
    """
    return render(request, 'first/scores.html', {
        'text':'안녕하세요',
        'scores' : scores2
    })