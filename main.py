import webapp2
import logging
import jinja2
import os

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class mainPage(webapp2.RequestHandler):
    def get(self):
        logging.info("Hi I am a logger")
        template = jinja_env.get_template("hello.html")
        self.response.write(template.render())
        # self.response.headers['Content-type'] = "Text Plain"
        # self.response.write("Hello world!")
        # self.reponse.write("<h2>Hello CSSI!<h2>")
        # self.reponse.write("<em>Hope you are having a fun time<em>")
        # self.reponse.write("<br><br>")

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
