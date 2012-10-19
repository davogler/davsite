from django.conf.urls.defaults import *

from coltrane.models import Entry

entry_info_dict = {'queryset':Entry.live.all(), 'date_field': 'pub_date', }

urlpatterns = patterns('',
# Pagination for the equivalent of archive_index generic view.
# The url is of the form http://host/page/4/
# In urls.py for example, ('^blog/page/(?P<page>\d)/$', get_archive_index),
	(r'^$', 'coltrane.views.get_archive_index_first', ),
	(r'^page/(?P<page>\d)/$', 'coltrane.views.get_archive_index', ),
	#(r'^$', 'django.views.generic.date_based.archive_index', entry_info_dict,  'coltrane_entry_archive_index'),
	(r'^(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', entry_info_dict, 'coltrane_entry_archive_year'),
	(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'django.views.generic.date_based.archive_month', entry_info_dict, 'coltrane_entry_archive_month'),
	(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'django.views.generic.date_based.archive_day', entry_info_dict, 'coltrane_entry_archive_day'),
	(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'django.views.generic.date_based.object_detail', entry_info_dict, 'coltrane_entry_detail'),
)