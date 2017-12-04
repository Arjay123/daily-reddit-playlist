sudo apt-get update &&
sudo apt-get -y upgrade &&
curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash - &&
sudo apt-get install -y nodejs python-pip python-dev libpq-dev postgresql postgresql-contrib &&
sudo pip install virtualenv &&
virtualenv env &&
source env/bin/activate &&
pip install -r requirements.txt  &&
sudo -u postgres psql -f dev_init.sql &&
cd app/ &&
npm install &&
python manage.py makemigrations --settings app.settings.dev_settings &&
python manage.py migrate --settings app.settings.dev_settings &&
python manage.py migrate --run-syncdb --settings app.settings.dev_settings