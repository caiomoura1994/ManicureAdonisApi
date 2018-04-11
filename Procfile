# web: python manage.py runserver 0.0.0.0:$PORT
web: gunicorn adonisapi.wsgi --log-file - --access-logfile - --error-logfile - --capture-output
