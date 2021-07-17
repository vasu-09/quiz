from django.shortcuts import render
from .models import Questions
# Create your views here.

def examination(request):
	context={}
	question=Questions.objects.all()
	context["question"]=question
	return render(request,'index.html', context)