from django.template import Library, Node
from django import template
from django.db.models import get_model
from coltrane.models import Category
     
register = Library()
register = template.Library()
     
class LatestContentNode(Node):
    def __init__(self, model, num, varname):
        self.num, self.varname = num, varname
        self.model = get_model(*model.split('.'))
    
    def render(self, context):
        context[self.varname] = self.model._default_manager.all()[:self.num]
        return ''
 
def get_latest(parser, token):
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError, "get_latest tag takes exactly four arguments"
    if bits[3] != 'as':
        raise TemplateSyntaxError, "third argument to get_latest tag must be 'as'"
    return LatestContentNode(bits[1], bits[2], bits[4])
    
get_latest = register.tag(get_latest)


def nav_categorylist():
	categories = Category.objects.all()
	return {'categories': categories}
	
register.inclusion_tag('coltrane/category_nav_list.html')(nav_categorylist)
