import webapp2
import logging

class mainPage(webapp2.RequestHandler):
    logging.info("Hi I am a logger");
    def get(self):
        # self.response.headers['Content-type'] = "Text Plain"
        self.response.write("Hello world!")

class secretPage(webapp2.RequestHandler):
    def get(self):
        # self.response.headers['Content-type'] = "Text Plain"
        self.response.write("Lorem ipsum")

class aboutPage(webapp2.RequestHandler):
    def get(self):
        # self.response.headers['Content-type'] = "Text Plain"
        self.response.write("This website is for testing Google's App engine.")

app = webapp2.WSGIApplication([
    ('/',mainPage),
    ('/secretentrance',secretPage),
    ('/about',aboutPage),
    ],debug=True
)
