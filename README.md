David Vogler's Personal Site
============================

Here lies the code behind my personal site, at a location soon to be disclosed.

Powered by Django, it features a categorized blog model and a simple image-based portfolio app.  The admin app employs Grappelli and Filebrowser.
The blog model is based loosely on [James Bennett's Coltrane app](http://www.amazon.com/gp/product/1590599969/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1590599969&linkCode=as2&tag=200e0a1-20), but has evolved somewhat.

### Running the Project

1. Clone the repository to your server. git clone git://github.com/davogler/davsite.git

2. Set up a virtual enviroment: mkvirtualenv mynewenv -r requirements.txt
(if using [Virtualenv](http://pypi.python.org/pypi/virtualenv) and [Virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/))

3. Create a private settings file `settings_private.py` and place it in the root directory:

        import sys
        globals().update(vars(sys.modules['settings']))
        
        ADMINS = ()
        MANAGERS = ADMINS
        DATABASES = {}
        SECRET_KEY = ''
        TIME_ZONE = ''
        GRAPPELLI_ADMIN_TITLE = ""
        INTERNAL_IPS = ()
        DISQUS_API_KEY = ''
        DISQUS_WEBSITE_SHORTNAME = ''
    
4. Set up your preferred database as declared in `settings_private.py`

5. Make sure the directory `media/uploads` exists

Development is ongoing, `DEBUG = Very True` Watch this space for updates.
