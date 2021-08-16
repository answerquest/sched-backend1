# commonfuncs.py

import uuid # for generating uid; replaces randomstring
import os, datetime, json, time, uuid, sys
import tornado.web
from tornado import concurrent

root = os.path.dirname(__file__) # needed for tornado
maxThreads = 8
inputFolder = os.path.join(root,'input')

logFolder = os.path.join(root,'logs')
os.makedirs(logFolder, exist_ok=True)

################################

def logmessage( *content ):
    timestamp = '{:%Y-%m-%d %H:%M:%S} :'.format(datetime.datetime.now())
    # from https://stackoverflow.com/a/26455617/4355695
    line = ' '.join(str(x) for x in list(content))
    # str(x) for x in list(content) : handles numbers in the list, converts them to string before concatenating. 
    # from https://stackoverflow.com/a/3590168/4355695
    print(line) # print to screen also
    f = open(os.path.join(logFolder,'serverlog.txt'), 'a', newline='\r\n', encoding='utf8') #open in append mode
    print(timestamp, line, file=f)
    # `,file=f` argument at end writes the line, with newline as defined, to the file instead of to screen. 
    # from https://stackoverflow.com/a/2918367/4355695
    f.close()


# handle file upload
def uploadaFile(fileholder):
    # adapted from https://techoverflow.net/2015/06/09/upload-multiple-files-to-the-tornado-webserver/
    # receiving a form file object as argument.
    filename = uuid.uuid4().hex
    full_filename = os.path.join(inputFolder,filename)
    with open(full_filename, "wb") as out:
        # Be aware, that the user may have uploaded something evil like an executable script ...
        # so it is a good idea to check the file content (xfile['body']) before saving the file
        out.write(fileholder['body'])
    return filename

def makeError(message, functionName='', code=400, amplitude=False):
    logmessage(message)
    return code, json.dumps({"status":"error","message":message})

def makeSuccess(returnD):
    returnD['status'] = 'success'
    if returnD.get('message'): logmessage(returnD['message'])
    return 200, json.dumps(returnD, default=str)


# for catching Ctrl+C and exiting gracefully. From https://nattster.wordpress.com/2013/06/05/catch-kill-signal-in-python/
def signal_term_handler(signal, frame):
	# to do: Make this work in windows, ra!
	logmessage('Closing Program, Bye')
	sys.exit(0)

