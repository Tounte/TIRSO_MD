from django.contrib import admin
from etat_stock.models import Clients,Transporteur,Destination,Origine

admin.site.register(Clients)
admin.site.register(Transporteur)
admin.site.register(Destination)
admin.site.register(Origine)


