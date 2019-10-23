from django.contrib import admin

from .models import Carnival, Grade, Place, Racetype, Register

# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
	list_display = ['event', 'race', 'bib']

admin.site.register(Carnival)
admin.site.register(Grade)
admin.site.register(Register, RegisterAdmin)
admin.site.register(Racetype)
admin.site.register(Place)
