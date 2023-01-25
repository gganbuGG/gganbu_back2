
from django.core.management.base import BaseCommand
import requests
from user.models import user


def delete_infoData():
    obj = user.objects.all()
    obj.delete()

class Command(BaseCommand):
    help = "Update 100 Ranker Data in the database to new Ranker Data."
    def handle(self, *args, **kwargs):
        delete_infoData()
        