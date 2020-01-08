from django.shortcuts import render
from alunos.forms import AlunoForm
from alunos.models import Aluno

# Create your views here.
def home(request):
    return render(request,'base.html')

def cadastrar_aluno(request):
    # instaciando o formulario -->
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        args = {
            'form':form, 
            'msg':'O cadastro foi realizado com sucesso :)'
        }
        return render(request, 'cadastro.html', args)
    args= {'form':form}  
    return render(request, 'cadastro.html', args)

def lista(request):
     lista_alunos = Aluno.objects.filter().all()



      