from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from contact.forms import RegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
def register(request):
   form =  RegisterForm()

   if request.method == 'POST':
      form =  RegisterForm(request.POST)

      if form.is_valid():
         form.save()
         messages.success(request,
            'Usuário registrado'
         )
         return redirect('contact:login')

      return render(
      request,
      'contact/register.html',
      {
         'form': form
      }
   )


   return render(
      request,
      'contact/register.html',
      {
         'form': form
      }
   )

@login_required(login_url='contact:login')
def user_update(request):
   form = UserUpdateForm(instance=request.user)
   
   if request.method == "POST":
      form = UserUpdateForm(data=request.POST, instance=request.user)
      if form.is_valid():
         form.save()
         messages.success(
            request,
            'Dados atualizados com sucesso'
         )
         return redirect(
            'contact:index'
         )

   
   
   return render(
      request,
      'contact/user_update.html',
      {
         'form': form
      }
   )


   
      
def login_view(request):

   form = AuthenticationForm(request)

   if request.method == "POST":
      form = AuthenticationForm(request, request.POST)

      if form.is_valid():
         user = form.get_user()
         print(user)
         auth.login(request, user)
         messages.success(request, 'Logado com sucesso')
         return redirect('contact:index')
      else:
         messages.error(request, 'Login inválido')
         return redirect('contact:login')
         
   return render(
      request,
      'contact/login.html',
      {
         'form': form
      }
   )

@login_required(login_url='contact:login')
def logout_view(request):
   auth.logout(request)
   return redirect(
     'contact:login'
   )