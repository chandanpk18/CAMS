from django.contrib import admin
from . import models


class EventAdmin(admin.ModelAdmin):
    list_display = ('event_name', 'event_manager_name', 'event_type', 'venue_selection', 'date_of_event', 'status')
    search_fields = ('event_name', 'event_type')
    list_filter = ('event_manager_name','status','date_of_event')


class HelpRequestAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'status')
    search_fields = ('username', 'email')
    list_filter = ('status',)


class UserAdmin(admin.ModelAdmin):
    search_fields = ('username', 'id')


admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Venue)
admin.site.register(models.Manager)
admin.site.register(models.HelpRequest, HelpRequestAdmin)
admin.site.register(models.users, UserAdmin)