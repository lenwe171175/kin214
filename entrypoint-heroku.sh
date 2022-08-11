echo "Making migrations"
python manage.py makemigrations || exit 1

echo "Running migrations for users database"
python manage.py migrate --database=users || exit 2

echo "Running migrations for spatial database"
python manage.py migrate --database=gadzmap || exit 3

echo "Inserting base data if necessary"
echo "import insert_base_data" | python manage.py shell || { echo "Missing super user configuration. Check the environment variables."; exit 4; }