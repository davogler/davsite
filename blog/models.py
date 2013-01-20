import datetime

from django.db import models

from django.contrib.auth.models import User
from markdown import markdown
from filebrowser.fields import FileBrowseField

class Category(models.Model):
	title = models.CharField(max_length=250, help_text='Max 250 characters.')
	slug = models.SlugField(unique=True, help_text='Auto-generated from title.  Must be unique.')
	description = models.TextField()
	
	class Meta:
		ordering = ['title']
		verbose_name_plural = "Categories"
	
	def live_entry_set(self):
		from blog.models import Entry
		return self.entry_set.filter(status=Entry.LIVE_STATUS)
	
	
	def __unicode__(self):
		return self.title
		
	def get_absolute_url(self):
		return ('blog_category_detail', (), { 'slug': self.slug })
		
	get_absolute_url = models.permalink(get_absolute_url)
		
	
class LiveEntryManager(models.Manager):
	def get_query_set(self):
		return super(LiveEntryManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)	
		
class Entry(models.Model):
	LIVE_STATUS = 1
	DRAFT_STATUS = 2
	HIDDEN_STATUS = 3
	STATUS_CHOICES = (
		(LIVE_STATUS, 'Live'),
		(DRAFT_STATUS, 'Draft'),
		(HIDDEN_STATUS, 'Hidden'),
	)
	title = models.CharField(max_length=250)
	excerpt = models.TextField(blank=True)
	excerpt_html = models.TextField(editable=False, blank=True)
	body = models.TextField()
	body_html = models.TextField(editable=False, blank=False)
	pub_date = models.DateTimeField()
	slug = models.SlugField(unique_for_date='pub_date')
	thumb = FileBrowseField("Thumbnail", max_length=200, directory="images/", extensions=[".jpg",".png", ".gif"], blank=True, null=True)
	pub_date = models.DateTimeField(default=datetime.datetime.now)
	author = models.ForeignKey(User)
	enable_comments = models.BooleanField(default=True)
	featured = models.BooleanField(default=False)
	
	status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
	categories = models.ManyToManyField(Category)

	live = LiveEntryManager()
	objects = models.Manager()	
	
	class Meta:
		ordering = ['-pub_date']
		verbose_name_plural = "Entries"
		
	def __unicode__(self):
		return self.title
		
	def save(self, force_insert=False, force_update=False):
		self.body_html = markdown(self.body)
		if self.excerpt:
			self.excerpt_html = markdown(self.excerpt)
		super(Entry, self).save(force_insert, force_update)
		
	def get_absolute_url(self):
		return ('blog_entry_detail', (), { 'year': self.pub_date.strftime('%Y'), 'month': self.pub_date.strftime('%b').lower(), 'day': self.pub_date.strftime('%d'), 'slug': self.slug })
	
	get_absolute_url = models.permalink(get_absolute_url)

		
class Link(models.Model):
	title = models.CharField(max_length=250)
	description = models.TextField(blank=True)
	description_html = models.TextField(editable=False, blank=True)
	url = models.URLField(unique=True)
	posted_by = models.ForeignKey(User)
	pub_date = models.DateTimeField(default=datetime.datetime.now)
	slug = models.SlugField(unique_for_date='pub_date')
	
	enable_comments = models.BooleanField(default=False)
	via_name = models.CharField('via', max_length=250, blank=True, help_text='The name of a person whose site you found this on. Optional.')
	via_url = models.URLField('via URL', blank=True, help_text='The URL of the site where you spotted this. Optional.')
	
	
	class Meta:
		ordering = ['-pub_date']
		
	def __unicode__(self):
		return self.title
		
	def save(self):
		if self.description:
			self.description_html = markdown(self.description)
		super(Link, self).save()
		
	def get_absolute_url(self):
		return ('blog_link_detail', (), { 'year': self.pub_date.strftime('%Y'),'month': self.pub_date.strftime('%b').lower(), 'day': self.pub_date.strftime('%d'), 'slug': self.slug })
	
	get_absolute_url = models.permalink(get_absolute_url)

		