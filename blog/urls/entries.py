from django.conf.urls.defaults import *
from django.views.generic.dates import YearArchiveView, MonthArchiveView, DayArchiveView, DateDetailView

from blog.models import Entry

entry_info_dict = {'queryset':Entry.live.all(), 'date_field': 'pub_date', }

urlpatterns = patterns('',
# Pagination for the equivalent of archive_index generic view.
# The url is of the form http://host/page/4/
# In urls.py for example, ('^blog/page/(?P<page>\d)/$', get_archive_index),
	url(r'^$', 'blog.views.get_archive_index_first', ),
	url(r'^page/(?P<page>\d)/$', 'blog.views.get_archive_index', ),
	#(r'^$', 'django.views.generic.date_based.archive_index', entry_info_dict,  'blog_entry_archive_index'),
	#(r'^(?P<year>\d{4})/$', YearArchiveView.as_view(), entry_info_dict, 'blog_entry_archive_year'),
	url(r'^(?P<year>\d{4})/$', YearArchiveView.as_view(**entry_info_dict), name= 'blog_entry_archive_year'),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', MonthArchiveView.as_view(**entry_info_dict), name= 'blog_entry_archive_month'),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', DayArchiveView.as_view(**entry_info_dict), name= 'blog_entry_archive_day'),
	url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', DateDetailView.as_view(**entry_info_dict), name= 'blog_entry_detail'),
)