echo "Making migrations"
python manage.py makemigrations || exit 1

echo "Running migrations for default database"
python manage.py migrate || exit 2

echo "Inserting base data if necessary"
echo "import insert_base_data" | python manage.py shell || { echo "Missing super user configuration. Check the environment variables."; exit 3; }