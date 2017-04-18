from django.contrib import admin


# Register your models here.
from firstapp.models import People,Aritcle

admin.site.register(People)
admin.site.register(Aritcle)