import webapp2
import os
import logging
from google.appengine.api import users
from google.appengine.ext.webapp import template

class Location(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        if users.get_current_user():
        	url = users.create_logout_url(self.request.uri)
        	url_linktext = 'Logout'
    	else:
    		url = users.create_login_url(self.request.uri)
    		url_linktext = 'Login'

    	template_values = {
    		'greetings': 'Hey',
    		'url': url,
    		'url_linktext': url_linktext
    		}
    	
    	path = os.path.join(os.path.dirname(__file__), 'tmp/location.html')    	    	
    	self.response.write(template.render(path, template_values))		

app = webapp2.WSGIApplication([('/location', Location),('/location/es', Location)], debug=True)
