import datetime

from django.db import models
from django.contrib.auth.models import User
from markdown import markdown
from filebrowser.fields import FileBrowseField


    
class Group(models.Model):
	title = models.CharField(max_length=250, help_text='Max 250 characters.')
	slug = models.SlugField(unique=True, help_text='Auto-generated from title.  Must be unique.')
	description = models.TextField()
    
	class Meta:
		db_table = "Group"
		verbose_name_plural = "Groups"
		ordering = ['title']
    
	def live_project_set(self):
		from work.models import Project
		return self.project_set.filter(status=Project.LIVE_STATUS)

	def __unicode__(self):
		return self.title
	
	def get_absolute_url(self):
		return ('work_group_detail', (), { 'slug': self.slug })
	
	get_absolute_url = models.permalink(get_absolute_url)
    

class LiveEntryManager(models.Manager):
	def get_query_set(self):
		return super(LiveEntryManager, self).get_query_set().filter(status=self.model.LIVE_STATUS)


class Project(models.Model):
	LIVE_STATUS = 1
	DRAFT_STATUS = 2
	STATUS_CHOICES = (
		(LIVE_STATUS, 'Live'),
		(DRAFT_STATUS, 'Draft'),
	)
	title = models.CharField(max_length=250)
	slug = models.SlugField(unique=True, help_text='Auto-generated from title.  Must be unique.')
	project_url = models.URLField('Project URL')
	description = models.TextField(blank=True)
	description_html = models.TextField(editable=False, blank=True)
	group = models.ManyToManyField(Group)
	completion_date = models.DateTimeField(default=datetime.datetime.now)
	weight = models.IntegerField()
	featured = models.BooleanField(default=False)
	thumb = FileBrowseField("Thumbnail", max_length=200, directory="images/", extensions=[".jpg",".png", ".gif"], blank=True, null=True)
	imagedir = FileBrowseField("Detail Directory", max_length=200, directory="images/", blank=True, null=True)
	detail_image1 = FileBrowseField("Image 1", max_length=200, directory="images/", extensions=[".jpg",".png", ".gif"], blank=True, null=True)
	detail_image2 = FileBrowseField("Image 2", max_length=200, directory="images/", extensions=[".jpg",".png", ".gif"], blank=True, null=True)
	detail_image3 = FileBrowseField("Image 3", max_length=200, directory="images/", extensions=[".jpg",".png", ".gif"], blank=True, null=True)
	detail_image4 = FileBrowseField("Image 4", max_length=200, directory="images/", extensions=[".jpg",".png", ".gif"], blank=True, null=True)
	detail_image5 = FileBrowseField("Image 5", max_length=200, directory="images/", extensions=[".jpg",".png", ".gif"], blank=True, null=True)
	detail_image6 = FileBrowseField("Image 6", max_length=200, directory="images/", extensions=[".jpg",".png", ".gif"], blank=True, null=True)
	status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
	live = LiveEntryManager()
	objects = models.Manager()

    
	class Meta:
		db_table = "Projects"
		ordering = ['weight']
		
	def __unicode__(self):
		return self.title
	
	def save(self):
		if self.description:
			self.description_html = markdown(self.description)
		super(Project, self).save()
	
	def get_absolute_url(self):
		return ('work_entry_detail', (), { 'slug': self.slug })

	get_absolute_url = models.permalink(get_absolute_url) 
