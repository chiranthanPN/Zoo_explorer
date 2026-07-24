from django.contrib import admin
from .models import animals, doner, caretaker

admin.site.register(animals)
admin.site.register(doner)
admin.site.register(caretaker)

