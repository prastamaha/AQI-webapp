# AQI (Air Quality Index) Web application

this application use django framework

## run application localhost

### create virtual env

    pip install venv
    python -m venv venv
    cd venv
    pip install django requests
    source venv/bin/activate

### clone repositoy

    git clone https://github.com/prastamaha/AQI-webapp.git 
    cd AQI-webapp

### running application
    
    python manage.py runserver

application will be running on [http://localhost:8000](http://localhost:8000)

## heroku deploy

setting.py

    DEBUG = False
    ALLOWED_HOSTS = ['air-qualityapp.herokuapp.com']
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'

visit this app:
[https://air-qualityapp.herokuapp.com](https://air-qualityapp.herokuapp.com)