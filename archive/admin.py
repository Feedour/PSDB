from django.contrib import admin
from .models import BG
from .models import Planet
from .models import Person
from .models import Mission

admin.site.register(BG)
admin.site.register(Planet)
admin.site.register(Person)
admin.site.register(Mission)

# Register your models here.
