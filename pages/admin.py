from django.contrib import admin
from .models import ContactRequest, Publications, Member, GroupInformation, ResearchField


class PublicationsAdmin(admin.ModelAdmin):
    ordering = ['-year']


class MembersAdmin(admin.ModelAdmin):
    ordering = ['-initial_year']


admin.site.register(GroupInformation)
admin.site.register(ResearchField)
admin.site.register(ContactRequest)
admin.site.register(Publications, PublicationsAdmin)
admin.site.register(Member, MembersAdmin)
