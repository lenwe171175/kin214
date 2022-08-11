if [ "$PROD" == "True" ]

then

echo "Making migrations"
python manage.py makemigrations || exit 1

echo "Running migrations for users database"
python manage.py migrate --database=users || exit 2

echo "Running migrations for spatial database"
python manage.py migrate --database=gadzmap || exit 3

echo "Inserting base data if necessary"
echo "import insert_base_data" | python manage.py shell || { echo "Missing super user configuration. Check the environment variables."; exit 4; }

echo "Collecting static files"
python3 manage.py collectstatic --noinput --clear

echo "Starting Server with Gunicorn"
gunicorn kin214.wsgi:application --bind 0.0.0.0:8000

else

echo "Making migrations"
python manage.py makemigrations || exit 1

echo "Running migrations for users database"
python manage.py migrate --database=users || exit 2

echo "Running migrations for spatial database"
python manage.py migrate --database=gadzmap || exit 3

echo "Inserting base data if necessary"
echo "import insert_base_data" | python manage.py shell || { echo "Missing super user configuration. Check the environment variables."; exit 4; }

echo "Starting Server"
python manage.py runserver 0:8000

fi