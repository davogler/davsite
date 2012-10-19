from django.shortcuts import get_object_or_404, render_to_response
from work.models import Group
from django.views.generic.list_detail import object_list

def group_detail(request, slug): 
	group = get_object_or_404(Group, slug=slug) 
	return object_list(request, queryset=group.live_project_set(), extra_context={ 'group': group})