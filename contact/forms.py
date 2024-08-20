from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact


class ContactForm(forms.ModelForm):

   first_name = forms.CharField(
      widget=forms.PasswordInput(
         attrs={
            'placeholder':'Digite o primeiro nome'
         }
      ), required=True,help_text="texto de ajuda"
   )
  
   class Meta:
      model = Contact
      fields = ('first_name','last_name','phone','email','description','category'
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


      self.add_error(
         'first_name',
         ValidationError(
            'Mensagem de erro',
            code='invalid'

         )
      )
      """
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
