from django.shortcuts import render, get_object_or_404
from .models import Quiz
# Create your views here.

def home(request):
  return render(request, 'main.html')

def Quizpage(request):
  q = Quiz.objects
  return render(request, 'Quizpage.html',{'quiz':q})

def Quizdetail(request, quiz_id):
  q = get_object_or_404(Quiz, pk = quiz_id)
  return render(request, 'Quizdetail.html',{'quiz':q})