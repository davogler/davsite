from django.contrib import admin
from tinymce.widgets import TinyMCE
from django import forms
from coltrane.models import Category, Entry, Link

class CategoryAdmin(admin.ModelAdmin): 
	prepopulated_fields = { 'slug': ['title'] }
	
admin.site.register(Category, CategoryAdmin)

class EntryAdminForm(forms.ModelForm):
	tiny = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label=u'Custom label', required=False)
	
	class Meta:
	    model = Entry


class EntryAdmin(admin.ModelAdmin): 
	prepopulated_fields = { 'slug': ['title'] }
	form = EntryAdminForm

	
admin.site.register(Entry, EntryAdmin)

class LinkAdmin(admin.ModelAdmin): 
	prepopulated_fields = { 'slug': ['title'] }

	
admin.site.register(Link, LinkAdmin)

