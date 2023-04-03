from django.contrib import admin
from .models import House, Apartment

# Register your models here.

# admin.site.register(House)
# admin.site.register(Apartment)


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('counryCode', 'city',
                    'street', 'house')

@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('house', 'apartment', 'square')

