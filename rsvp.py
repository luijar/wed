import webapp2
import os
import cgi
import logging
from google.appengine.api import users
from google.appengine.ext.webapp import template

class RSVP(webapp2.RequestHandler):
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
    	
    	path = os.path.join(os.path.dirname(__file__), 'tmp/rsvp.html')    	    	
    	self.response.write(template.render(path, template_values))		
    
    def post(self):      
        self.response.headers['Content-Type'] = 'text/html'

        first_name = cgi.escape(self.request.get('first-name'))
        last_name = cgi.escape(self.request.get('last-name'))
        email = cgi.escape(self.request.get('email'))
        guests = cgi.escape(self.request.get('guests'))
        country = cgi.escape(self.request.get('country'))
        message = cgi.escape(self.request.get('last-name'))

        template_values = {
            'greetings': 'Hey'            
        }

        path = os.path.join(os.path.dirname(__file__), 'tmp/confirm.html')             
        self.response.write(template.render(path, template_values))     

app = webapp2.WSGIApplication([('/rsvp', RSVP),('/rsvp/es', RSVP)], debug=True)
