from django.conf.urls.defaults import *
from work.models import Project, Group

project_info_dict = {'queryset':Project.objects.all(), }

urlpatterns = patterns('',
	(r'^groups/$', 'django.views.generic.list_detail.object_list', {'queryset':Group.objects.all() }, 'work_group_list'),
	(r'^group/(?P<slug>[-\w]+)/$', 'work.views.group_detail', {}, 'work_group_detail'),
	(r'^$', 'django.views.generic.list_detail.object_list', dict(project_info_dict)),
	(r'^(?P<slug>[-\w]+)/$', 'django.views.generic.list_detail.object_detail', dict(project_info_dict, slug_field='slug'), 'work_entry_detail'),
)
