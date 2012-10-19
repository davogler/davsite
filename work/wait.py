class Project(models.Model):
	LIVE_STATUS = 1
	DRAFT_STATUS = 2
	STATUS_CHOICES = (
		(LIVE_STATUS, 'Live'),
		(DRAFT_STATUS, 'Draft'),
	)
	title = models.CharField(maxlength=250)
	slug = models.SlugField(prepopulate_from=('name',))
	project_url = models.URLField('Project URL')
	description = models.TextField(blank=True)
	description_html = models.TextField(editable=False, blank=True)
	group = models.ManyToManyField(Group)
	completion_date = models.DateTimeField(default=datetime.datetime.now)
	weight = models.IntegerField()
	featured = models.BooleanField(default=False)
	overview_image = models.URLField()
	detail_image = models.URLField()
	status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
	categories = models.ManyToManyField(Category)
	live = LiveEntryManager()
	objects = models.Manager()	
    
    
	class Meta:
		db_table = "Projects"
		ordering = ['weight']
		
	class Admin:
		pass
	
	def __unicode__(self):
		return self.title
	
	def save(self):
		if self.description:
			self.description_html = markdown(self.description)
		super(Project, self).save()
	
	def get_absolute_url(self):
		return ('work_entry_detail', (), { 'slug': self.slug })

	get_absolute_url = models.permalink(get_absolute_url) 
