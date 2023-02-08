from django.contrib import admin
from .models import user,match,static

class matchAdmin(admin.ModelAdmin):
    search_fields=('Name__name',)

admin.site.register(match, matchAdmin)

