from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    #custom admin area
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listings')
    list_per_page = 25
admin.site.register(Contact, ContactAdmin)
