import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')

import django
django.setup()

#FAKE UP ScripT
import random
from firstapp.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','social market','News','games']

def add_topic():
    t = Topic.objects.get_or_create(Top_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for entry in range(N):

        #get the topic for entry
        top = add_topic()

        #create the fake data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name= fake_name)[0]

        #create fake AccessRecord entry
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == "__main__":
    print("populating ScripT")
    populate(10)
    print("populating completed!")
