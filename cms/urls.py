from django.conf.urls.defaults import *
from filebrowser.sites import site
from django.conf import settings
from blog.models import Entry
from blog.feeds import CategoryFeed, LatestEntriesFeed, LatestLinksFeed
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

feeds = { 'entries': LatestEntriesFeed,
          'categories': CategoryFeed,
          'links': LatestLinksFeed }

from django.contrib import admin
admin.autodiscover()

featured_entry_info_dict = {'queryset':Entry.objects.filter(featured=True), 'date_field': 'pub_date',}

urlpatterns = patterns('',
    # Example:
    # (r'^cms/', include('cms.foo.urls')),
    (r'^$', 'blog.views.get_featured', ),
    (r'^admin/filebrowser/', include(site.urls)),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/', include(admin.site.urls)),
	(r'^search/$', 'cms.search.views.search'), 
	(r'^blog/categories/', include('blog.urls.categories')),
	(r'^blog/links/', include('blog.urls.links')),
	
	(r'^blog/', include('blog.urls.entries')),
	(r'^comments/', include('django.contrib.comments.urls')),
	(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.Feed', { 'feed_dict': feeds }),
	(r'^work/', include('work.urls')),
	#(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
	(r'^master.html/$', 'views.masterview'),
	#(r'^templates/master.html$', 'views.masterview'),
	
	
)

urlpatterns += staticfiles_urlpatterns()
