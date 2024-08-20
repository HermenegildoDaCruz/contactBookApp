import os
import sys

from datetime import datetime
from pathlib import Path
from random import choice


import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent#Será usado para ajudar importar coisas da raíz do projecto

NUMBER_OF_OBJECTS = 500

#____________Para dizer ao django que a pasta utils também faz parte do projecto
sys.path.append(str(DJANGO_BASE_DIR))# Permite importar coisas da raíz do projecto para frente
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings' # Registrando esse modulo como parte do projeto
settings.USE_TZ = False

django.setup()# Inicializando o django daqui para baixo, isso permite trabalhar com models a partir desse modulo
#_________________________________________

#Se o modulo for executado com principal ou main:

if __name__ == "__main__":
   import faker
   from contact.models import Category,Contact

   Contact.objects.all().delete()
   Category.objects.all().delete()

   fake = faker.Faker('pt')

   categories = ['Amigo','Familiar','Conhecido']

   django_categories = [Category(name = name) for name in categories]
   for category in django_categories:
      category.save()

   django_contacts = []
   for _ in range(NUMBER_OF_OBJECTS):
      profile = fake.profile()
      email = profile['mail']
      first_name, last_name = profile['name'].split(' ',1)
      phone = fake.phone_number()
      created_date :datetime = fake.date_this_year()
      description = fake.text(max_nb_chars = 100)
      category = choice(django_categories)

      django_contacts.append(
         Contact(
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            email = email,
            created_date = created_date,
            description = description,
            category = category
         )

      )

#Criando os contactos com o bulk_create
if len(django_contacts) > 0:
   Contact.objects.bulk_create(django_contacts)