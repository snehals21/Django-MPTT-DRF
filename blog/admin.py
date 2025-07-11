from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin


admin.site.register(models.Book)

# following is the MPTT model registration.
admin.site.register(models.Chapter, MPTTModelAdmin)
