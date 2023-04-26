from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import User,Perfil
from .forms import PerfilForm
from posts.models import FollowersCount

@login_required(login_url='/users/login')
def Perfil_user(resquest):

    perfiles  = Perfil.objects.filter(user=resquest.user)
   

    if resquest.method == 'POST':
        form = PerfilForm(resquest.POST or None,resquest.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('users:perfil')
    else:
        form = PerfilForm()
    return render(resquest,'perfil.html',{'form':form,'perfiles':perfiles})




def perfiles_all(request):
    perfiles = Perfil.objects.all().exclude(user=request.user)
    return render(request,'perfiles_all.html',{'perfiles':perfiles})



def perfiles(request, id):
    usuario = User.objects.get(id=id)
    seguidores = FollowersCount.objects.filter(siguiendo_a=usuario).count()
   
    perfiles_of_users = Perfil.objects.filter(user=usuario)
    
    sigue_usuario = FollowersCount.objects.filter(seguidor=request.user, siguiendo_a=usuario).exists()

    context = {'perfiles_of_users':perfiles_of_users,
               'usuario':usuario,
               'seguidores':seguidores,
               'sigue_usuario':sigue_usuario}

    return render(request,'perfiles.html', context)


def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST.get('password2')
        user = User.objects.filter(username=username).exists()

        if user :
            return redirect('login')

        if password1 == password2:
            user = User.objects.create_user(username=request.POST['username'],
                                            password= request.POST['password1'])
            user.save()
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
        
    else:
        return render(request,'register.html')


def IniciaSession(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        user = User.objects.filter(username=username).exists()

        if user:
            user = authenticate(request,username=username,password=password1,)
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
        else:
            return redirect('users:register')
           
    else:
        return render(request,'login.html')
    

def logoute(request):
     logout(request)
     return redirect('users:login')