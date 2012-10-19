from django.contrib import admin
from work.models import Group, Project

class GroupAdmin(admin.ModelAdmin): 
	prepopulated_fields = { 'slug': ['title'] }
	
admin.site.register(Group, GroupAdmin)

class ProjectAdmin(admin.ModelAdmin): 
	prepopulated_fields = { 'slug': ['title'] }

	
admin.site.register(Project, ProjectAdmin)


