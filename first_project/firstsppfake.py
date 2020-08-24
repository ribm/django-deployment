import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from firstapp.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen = Faker()

topics = ['Search', 'social', 'Sports','Politics']

def add_topic():
    t= Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for i in range(N):
        
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        wepg = Webpage.objects.get_or_create(Topic=random.choice(topics),name=fake_name,url=fake_url)[0]
        acred = AccessRecord.objects.get_or_create(name=fake_name,date=fake_date)[0]


if __name__=='__main__':
    print("start")
    populate(N=10)
    print("done")