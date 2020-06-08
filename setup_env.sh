. env/bin/activate
echo '========================= Installing python3 and pip3 ==============================='
echo 'y' | apt install python3
echo 'y' | apt install python3-pip
echo 'y' | apt install pylint

echo '========================= Installing Flask and Flask-RESTful ========================'
echo 'y' | pip install Flask
echo 'y' | pip install Flask-RESTful

echo '========================= Installing SQLAlchemy ====================================='
echo 'y' | pip install Flask-SQLAlchemy
echo 'y' | pip install flask-marshmallow
echo 'y' | apt install unixodbc-dev
echo 'y' | pip install pyodbc

echo '========================= Installing ODBC Driver 17 for SQL Server ====================================='
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
curl https://packages.microsoft.com/config/ubuntu/19.10/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
sudo ACCEPT_EULA=Y apt-get install msodbcsql17
sudo ACCEPT_EULA=Y apt-get install mssql-tools
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc
sudo apt-get install unixodbc-dev
