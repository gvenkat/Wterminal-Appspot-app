import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
  def get(self):
    template_vars = { }
    path = os.path.join(os.path.dirname(__file__), 'doc.html')
    self.response.out.write(template.render(path, template_vars))


class DemoPage( webapp.RequestHandler ):
  def get( self ):
    template_vars = { }
    path = os.path.join(os.path.dirname(__file__), 'test.html')
    self.response.out.write(template.render(path, template_vars))

application = webapp.WSGIApplication(
                                     [
                                       ('/', MainPage),
                                       ('/demo', DemoPage)
                                     ],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
