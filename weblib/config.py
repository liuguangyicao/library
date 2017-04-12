CSRF_ENABLED = True
SECRET_KEY = '51258868lin'
import os
basedir = os.path.abspath(os.path.dirname(__file__))
UPLOADED_IMAGES_DEST = os.getcwd()+'/app/static'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
