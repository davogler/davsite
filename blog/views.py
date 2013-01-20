from django.shortcuts import get_object_or_404, render_to_response
from blog.models import Category
from django.views.generic.list_detail import object_list

def category_detail(request, slug): 
	category = get_object_or_404(Category, slug=slug) 
	return object_list(request, queryset=category.live_entry_set(), extra_context={ 'category': category})
	
from django.core.paginator import Paginator
from django.views.generic.list_detail import object_list
from django.http import Http404
from django.shortcuts import get_list_or_404
from blog.models import Entry

num_in_page = 4

# Pagination for the equivalent of archive_index generic view.
# The url is of the form http://host/page/4/
# In urls.py for example, ('^blog/page/(?P<page>\d)/$', get_archive_index),
def get_archive_index(request, page):
    queryset = Entry.live.all()
    paginator = Paginator(queryset, num_in_page)
    
    try:
    	page = int(page)
    except ValueError:
    	page = int(1)
    
 
    if int(page) in paginator.page_range:
    	listy = paginator.page(page)
    	return object_list(request, queryset, paginate_by=num_in_page, page=int(page), extra_context={ 'listy': listy}, template_name='blog/entry_archive_paged.html')
    # send a 404 error that page is not found.
    raise Http404

    
def get_archive_index_first(request):
    #view for the first page of the blog (no page #)
    queryset = Entry.live.all()
    paginator = Paginator(queryset, num_in_page)
    listy = paginator.page(1)
    return object_list(request, queryset, paginate_by=num_in_page, page=int(1), extra_context={ 'listy': listy}, template_name='blog/entry_archive_paged.html')
    
from django.conf import settings
from django.shortcuts import render_to_response

def get_featured(request):
    queryset = Entry.live.filter(featured=True)[:2]
    return object_list(request, queryset, template_name='home.html')



