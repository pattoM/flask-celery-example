class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ''
    SECRET_KEY = 'dbbc933946e04a729b17c0625b72e3db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USERNAME = ''
    MAIL_PASSWORD = '' 
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_SUPPRESS_SEND = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = '' #get this from cloud amqp 
    YT_API_KEY = "" #youtube api key
    HOST_PLAYLISTS = ["PLiQ766zSC5jPIKibTa5qtXpwgwEBalDV4","PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX","PLl0KD3g-oDOHElCF7S7q6CRGz1qG8vQkS"] 

    
