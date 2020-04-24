from django.contrib import admin
from .models import ContactRequest, Publications, Member, GroupInformation, ResearchField
from tinymce.widgets import TinyMCE
from django.db import models


class PublicationsAdmin(admin.ModelAdmin):
    ordering = ['-year']


class MembersAdmin(admin.ModelAdmin):
    ordering = ['-initial_year']
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


class ResearchFieldAdmin(admin.ModelAdmin):
	formfield_overrides = {
	    models.TextField: {'widget': TinyMCE()},
	}


class GroupInformationAdmin(admin.ModelAdmin):
 	formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


admin.site.register(GroupInformation, GroupInformationAdmin)
admin.site.register(ResearchField, ResearchFieldAdmin)
admin.site.register(ContactRequest)
admin.site.register(Publications, PublicationsAdmin)
admin.site.register(Member, MembersAdmin)
