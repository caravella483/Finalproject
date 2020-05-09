import os

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KEY') or "fInAL_proJEct"
    
dbusername = ""
dbpassword = ""