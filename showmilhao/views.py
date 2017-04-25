from django.shortcuts import render
from .models import Questao

# Create your views here.

def post_list(request):
    questoes = Questao.objects.all()
    return render(request, 'showmilhao/post_list.html', {
        'questoes': questoes)

