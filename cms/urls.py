from django.conf.urls.defaults import *
from django.conf import settings
from coltrane.models import Entry
from coltrane.feeds import CategoryFeed, LatestEntriesFeed, LatestLinksFeed

feeds = { 'entries': LatestEntriesFeed,
          'categories': CategoryFeed,
          'links': LatestLinksFeed }

from django.contrib import admin
admin.autodiscover()

featured_entry_info_dict = {'queryset':Entry.objects.filter(featured=True), 'date_field': 'pub_date',}

urlpatterns = patterns('',
    # Example:
    # (r'^cms/', include('cms.foo.urls')),
    (r'^$', 'coltrane.views.get_featured', ),
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    #(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
	#			{ 'document_root': settings.TINYMCE_ROOT }),
	(r'^search/$', 'cms.search.views.search'), 
	(r'^blog/categories/', include('coltrane.urls.categories')),
	(r'^blog/links/', include('coltrane.urls.links')),
	
	(r'^blog/', include('coltrane.urls.entries')),
	(r'^comments/', include('django.contrib.comments.urls')),
	(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', { 'feed_dict': feeds }),
	(r'^work/', include('work.urls')),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
	(r'^master.html/$', 'views.masterview'),
	#(r'^templates/master.html$', 'views.masterview'),
	
	
)
