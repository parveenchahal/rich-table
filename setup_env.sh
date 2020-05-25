. env/bin/activate
echo '========================= Installing python3.6 and pip ================================'
echo 'y' | apt-get install python3.6
echo 'y' | apt-get install python3-pip

echo '========================= Installing Flask and Flask-RESTful =========================='
echo 'y' | pip install Flask
echo 'y' | pip install Flask-RESTful
