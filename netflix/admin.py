from django.contrib import admin
from netflix.models import Director
from netflix.models import Film,characters
# Register your models here.

class FilmAdmin(admin.ModelAdmin):
    filter_horizontal =('characters',)

admin.site.register(Director)
admin.site.register(Film,FilmAdmin)
admin.site.register(characters)