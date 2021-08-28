openBrowser = True
# server_launch.py

import os, sys, json, urllib, time, datetime, signal
import tornado.web
from tornado import concurrent
from tornado import escape
import webbrowser

import commonfuncs as cf
import mainprog

print('Loaded dependencies, starting program.')

###########################
# setting constants
portnum = 5000
maxThreads = 8
root = os.path.dirname(__file__) # needed for tornado
print("root:",root)

maxFileSize = 10485760000 # in bytes, used to set maximum file size of uploads. Default: 100MB = 104857600 bytes

inputFolder = os.path.join(root,'input')
os.makedirs(inputFolder, exist_ok=True)


###########################
# Define all API call classes here

class upload(tornado.web.RequestHandler):
    executor = concurrent.futures.ThreadPoolExecutor(maxThreads)

    @tornado.gen.coroutine
    def post(self):
        status, result = yield self.post_function() 
        self.set_status(status)
        self.write(result)

    @tornado.concurrent.run_on_executor 
    def post_function(self):
        cf.logmessage('upload api call')
        returnD = {}
        if not len(self.request.files):
            return cf.makeError("No file uploaded")
        
        configD = {}
        
        fileHolder = self.request.files['attachment'][0]
        input_filename = cf.uploadaFile(fileHolder)
        configD['attachment'] = input_filename

        configD['maxDelay'] = float(self.get_body_argument('maxDelay', default=5))
        configD['maxRunning'] = float(self.get_body_argument('maxRunning', default=16))
        configD['travelTime'] = float(self.get_body_argument('travelTime', default=1))

        cf.logmessage(configD)

        returnD = mainprog.computeThis(configD)

        cf.logmessage(returnD)

        return cf.makeSuccess(returnD)


class test(tornado.web.RequestHandler):
    def get(self):
        print("yes the program is working")
        self.set_status(200)
        self.write("Ok I see you")


###################
# List API calls and the class they will be directed to, here
def make_app():
    return tornado.web.Application([
        #(r"/API/data", APIHandler),
        (r"/API/upload", upload),
        (r"/API/test", test),
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": root, "default_filename": "index.html"})
    ])


###################################################         
# Now, at last, the __main__ function sets up the tornado server

if __name__ == "__main__":
    signal.signal(signal.SIGINT, cf.signal_term_handler)
    app = make_app()
    while True: # loop to increment the port number till we find one that isn't occupied
        try:
            port = int(os.environ.get("PORT", portnum))
            # app.listen(port)
            server = tornado.httpserver.HTTPServer(app, max_buffer_size=maxFileSize) # setting maximum file size of uploads
            server.listen(port)
            break
        except OSError:
            portnum += 1
            if portnum > 9999: 
                print('Thats it I give up! From 5000 to 9999 not a single port number is free! Can\'t run your server, sorry!')
                sys.exit()

    thisURL = "http://localhost:" + str(port)
    if openBrowser: webbrowser.open(thisURL)
    print("Open " + thisURL + " in your Web Browser if you don't see it opening automatically within 5 seconds.")
    tornado.ioloop.IOLoop.current().start()
