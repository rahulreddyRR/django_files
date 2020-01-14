import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","protwo.settings")

import django
django.setup()

from firstapp.models import User
from faker import Faker

fakegen = Faker()

def fake(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(First_name=fake_first_name,
                                            Last_name=fake_last_name,
                                            Email=fake_email)[0]
if __name__== '__main__' :
    print("populating")
    fake(10)
    print("populating completed!")
