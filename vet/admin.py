from django.contrib import admin
from .models import Profile, Animal, Appointment, Medication, Note

# Register the models so they show up in the admin interface
admin.site.register(Profile)
admin.site.register(Animal)
admin.site.register(Appointment)
admin.site.register(Medication)
admin.site.register(Note)
