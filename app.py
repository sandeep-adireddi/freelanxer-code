import flask
from tweet_processing import tweet_stream_controller 
import time
from flask import request
app = flask.Flask(__name__)
	
class Controller:

	def start(self):
		try:
			args = request.args
			self.tweet_stream_controller = tweet_stream_controller(args['keyword'])
			self.tweet_stream_controller.start_stream()
			return "Server is processing tweets"
		except Exception as e:
	    	return(str(e))

	def end(self):
		try:
			self.tweet_stream_controller.end_stream()
			return "Server ended processing tweets"
		except Exception as e:
	    	return(str(e))

Controller = Controller()

app.add_url_rule('/start','start',lambda:Controller.start())
app.add_url_rule('/end','end',lambda:Controller.end())

if __name__ == '__main__':
    app.run(debug=True)