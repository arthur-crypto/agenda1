from django.contrib import admin
from core.models import Eventos

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display =('titulo', 'data_evento', 'data_criação')
    list_filter = ('titulo', 'data_evento',)

admin.site.register(Eventos, EventoAdmin)