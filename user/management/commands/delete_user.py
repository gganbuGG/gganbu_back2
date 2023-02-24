
from django.core.management.base import BaseCommand
import requests
from user.models import user,match,state


def delete_infoData():
    obj = state.objects.all()
    obj.delete()


    

class Command(BaseCommand):
    help = "Update 100 Ranker Data in the database to new Ranker Data."
    def handle(self, *args, **kwargs):
        delete_infoData()
       
        