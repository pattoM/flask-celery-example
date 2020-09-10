web: gunicorn app:app 
hybrid_worker: celery -A app.celery  worker --beat --loglevel=info 