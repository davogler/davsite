from django.contrib import admin
from django import forms
from blog.models import Category, Entry

class CategoryAdmin(admin.ModelAdmin): 
	prepopulated_fields = { 'slug': ['title'] }
	
admin.site.register(Category, CategoryAdmin)

class EntryAdminForm(forms.ModelForm):
	
	class Meta:
	    model = Entry

class EntryAdmin(admin.ModelAdmin): 
	prepopulated_fields = { 'slug': ['title'] }
	form = EntryAdminForm

	
admin.site.register(Entry, EntryAdmin)

