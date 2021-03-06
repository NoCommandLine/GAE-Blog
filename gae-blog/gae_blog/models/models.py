import logging
logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
	datefmt='%Y-%m-%d:%H:%M:%S',
	level=logging.INFO) 
logger = logging.getLogger(__name__)
import datetime
from google.cloud import ndb
PAGE_SIZE = 25


class BlogPosts(ndb.Model):
	title = ndb.StringProperty(required=True)
	body = ndb.TextProperty(required=True)
	imageURL = ndb.StringProperty() 
	imageTitle = ndb.StringProperty() 
	isDraft = ndb.BooleanProperty(default=True)
	slug = ndb.StringProperty(required=False)
	created = ndb.DateTimeProperty(auto_now_add=True)
	lastModified = ndb.DateTimeProperty(auto_now=True) 
	publishDate = ndb.DateTimeProperty()
	seo_keywords = ndb.StringProperty(required=False, repeated=True)
	summary = ndb.StringProperty()

	
	@classmethod
	def getPublished(cls, page=None):
		try:
			page = ndb.Cursor.from_websafe_string(page) if page else ndb.Cursor()
			return cls.query(cls.isDraft == False).order(-cls.publishDate).fetch_page(PAGE_SIZE, start_cursor=page)

		except Exception as e:
			logger.info('An error occured')
			logger.error(e)
			return "Error", None, None


	@classmethod
	def getPublishedByDate(cls, year, month, page=None):
		minDate = datetime.datetime(year, month, 1)
		if minDate.month == 12:
			year = year + 1
			month = 1
		else:
			month = minDate.month + 1
		maxDate = datetime.datetime(year, month, 1)

		
		try:
			page = ndb.Cursor.from_websafe_string(page) if page else ndb.Cursor()
			return cls.query(cls.isDraft == False, cls.publishDate >= minDate, cls.publishDate < maxDate).order(-cls.publishDate).fetch_page(PAGE_SIZE, start_cursor=page)

		except Exception as e:
			logger.info('An error occured')
			logger.error(e)
			return "Error", None, None


	@classmethod
	def getBySlug(cls, slug):
		return cls.query(cls.slug == slug, cls.isDraft == False).get()


	@classmethod
	def getForSitemap(cls):
		return cls.query(cls.isDraft == False).order(-cls.publishDate).fetch(projection=[cls.slug, cls.publishDate])

		

class Comments(ndb.Model):
	post = ndb.KeyProperty(kind = "BlogPost") 
	authorName = ndb.StringProperty(required=True)
	authorEmail = ndb.StringProperty()
	authorWebsite = ndb.StringProperty()
	comment = ndb.TextProperty(required=True)
	isDraft = ndb.BooleanProperty(default=True)
	created = ndb.DateTimeProperty(auto_now_add=True) 