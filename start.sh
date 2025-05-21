python manage.py migrate
python manage.py collectstatic --noinput
gunicorn urchin_mall.wsgi:application --bind 0.0.0.0:8000