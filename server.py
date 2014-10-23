import tornado.httpserver
import tornado.web
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('welcome')
	def post(self):
		print self.request.body
		name = self.get_argument('name')
		city = self.get_argument('city')
		self.write('hello ' + name + ' from ' + city)

app = tornado.web.Application([
	(r'/', MainHandler),
])

server = tornado.httpserver.HTTPServer(app)
server.listen(8000)
print 'server listening on localhost port 8000 ...'
tornado.ioloop.IOLoop().instance().start()
