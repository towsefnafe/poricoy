from django.contrib import admin
from .models import Skill, Work, Portfolio, Service, Contact

# Register your models here.
admin.site.register(Skill)
admin.site.register(Work)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Portfolio)
