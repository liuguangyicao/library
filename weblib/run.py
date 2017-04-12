from app import app
from flask_wtf.csrf import CSRFProtect
if __name__ == '__main__':
    csrf = CSRFProtect(app)
    app.run(debug = False,threaded=True,host='0.0.0.0')
    
#,port=8080,host='0.0.0.0'
