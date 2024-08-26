from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
class ContactForm(forms.ModelForm):

   picture = forms.ImageField(
      widget= forms.FileInput(
         attrs={
            'accept': 'image/*'
         }
      )
   )
   class Meta:
      model = Contact
      fields = ('first_name','last_name','phone','email','description','category','picture'
         )
      """
      widgets = {
         'first_name': forms.PasswordInput(
            attrs={
               'placeholder': 'Digite algo'
            }
         )
      }"""

   def clean(self):
      #print(self.cleaned_data)

      """
      self.add_error(
         'first_name',
         ValidationError(
            'Mensagem de erro',
            code='invalid'

         )
      )
     
      self.add_error(
         None,
         ValidationError(
            'Mensagem de erro',
            code='invalid'

         )
      )"""
      return super().clean()
   
   def clean_first_name(self):
      first_name = self.cleaned_data.get('first_name')

      if first_name == "ABD":
         self.add_error(
            'first_name',
            ValidationError(
               'Não digite ABD',
               code='invalid'
            )
         )
         return None

      return first_name

class RegisterForm(UserCreationForm):

   first_name = forms.CharField(
      required=True,
      min_length=2,
      max_length=30,
      help_text='required.',
      error_messages={
         'min_length': 'Por favor, insira mais de 2 letras'
      }
   )
   last_name = forms.CharField(
      required=True,
      min_length=2,
      max_length=30,
      help_text='required.'
   )
   email = forms.EmailField()

   
   class Meta:
      model = User
      fields = 'first_name','last_name','email','username','password1','password2',
      

   def clean_email(self):
      email = self.cleaned_data.get('email')

      if User.objects.filter(email=email).exists():
         self.add_error(
            'email',
            ValidationError(
               'Este email já existe', code='Invalid'
            )
         )
      return email
   
class UserUpdateForm(forms.ModelForm):

   first_name = forms.CharField(
      required=True,
      min_length=2,
      max_length=30,
      help_text='required.',
      error_messages={
         'min_length': 'Por favor, insira mais de 2 letras'
      }
   )
   last_name = forms.CharField(
      required=True,
      min_length=2,
      max_length=30,
      help_text='required.'
   ) 
   password1 = forms.CharField(
      label="Password",
      strip=False,
      widget=forms.PasswordInput(
         attrs={
            'autocomplete': 'new_password'
         } 
      ),
      help_text= password_validation.password_validators_help_text_html(),
      required=False

   )
   password2 = forms.CharField(
      label="Password 2",
      strip=False,
      widget=forms.PasswordInput(
         attrs={
            'autocomplete': 'new_password'
         } 
      ),
      help_text= 'Usa a mesma palavra-passe como a de cima',
      required=False

   )
   class Meta:
      model = User
      fields = 'first_name','last_name','email','username'

   #Resolvendo problema de atualizacao do email
   def clean_email(self):
      email = self.cleaned_data.get('email')
      current_email = self.instance.email#Para pegar o email do user(instance)

      if email == current_email:
         return email
      
      else:
         if User.objects.filter(email=email).exists():
            self.add_error(
               'email',
               ValidationError(
                  'Email já Existe', code='Invalid'
               )
            )
      
      #Se o email passado for vazio ele retorna o email do usuario
      if email.strip() == "":
         return current_email
      
      return email
   
   def save(self, commit = True):
      cleaned_data = self.cleaned_data
      user = super().save(commit=False)

      password = cleaned_data.get('password1')

      if password:
         user.set_password(password)

      if commit:
         user.save()
         return user
   def clean(self):
      password1 = self.cleaned_data.get('password1')
      password2 = self.cleaned_data.get('password2')

      if password1 or password2:
         if password2 != password1:
            self.add_error(
               'password2',
               ValidationError(
                  'Senhas não batem', code='invalid'
               )
            )
      return super().clean()
   
   def clean_password(self):
      password1 = self.cleaned_data.get('password1')

      if password1:
         try:
            password_validation.validate_password(password1)
         except ValidationError as error:
            self.add_error(
               'password1',
               ValidationError(
                  error, code='invalid'
               )
            )

      return password1
   

