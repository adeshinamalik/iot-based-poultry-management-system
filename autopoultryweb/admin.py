from django.contrib import admin
from autopoultryweb.models import EggCollection, WasteCollection, Feeding, Water

# Register your models here.
admin.site.register(EggCollection)
admin.site.register(WasteCollection)
admin.site.register(Feeding)
admin.site.register(Water)
