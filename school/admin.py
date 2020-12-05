from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(subject)
admin.site.register(student_profile)
admin.site.register(geographie)
admin.site.register(math)
admin.site.register(science)
admin.site.register(religous_studie)
admin.site.register(art)
admin.site.register(attendence)
admin.site.register(teacher)