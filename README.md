# Website "Nordic walking"
The following actions were performed on ubuntu 19.04 and python 3.6.

> HTML/CSS and part of JS made another person, not me.


### **Getting started**
* [Initial actions](#initial-actions)
* [MYSQL](#mysql)
    * [Installing MYSQL](#installing-mysql)
    * [Creating DB](#creating-db-for-django-application)
* [NGINX + UWSGI](#nginx--uwsgi)
    * [Setting domen name](#setting-domen-name)
    * [NGINX](#nginx)
    * [Adding SSL](#adding-ssl)
    * [UWSGI](#uwsgi)
* [Security settings](#security-settings)
    * [Fail2Ban](#fail2ban)
    

## Initial actions
```bash
# - Installing require packages -
apt-get update
sudo apt-get install build-essential zlib1g-dev python3-dev virtualenv libssl-dev libffi-dev python3-dev python3-venv \
    libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev \
    mysql-server libmysqlclient-dev nginx unzip

adduser django
usermod -aG sudo django
su django
cd

# - Installing python -
wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tar.xz
tar -xvf Python-3.6.8.tar.xz && rm Python-3.6.8.tar.xz
cd Python-3.6.8/
./configure && make && sudo make altinstall
cd ..

# --- Setting up Django app ---
# - For test -
git clone --single-branch --branch devel https://github.com/mkbeh/website_nordic_walking

# - For production -
git clone https://github.com/mkbeh/website_nordic_walking

cd website_nordic_walking/
python3.6 -m venv venv
source venv/bin/activate
python3.6 -m pip install -r requirements.txt

# - Setting the lifetime of the sss session -
# - Uncomment next lines in /etc/ssh/sshd_config -
TCPKeepAlive yes
ClientAliveInterval 300
ClientAliveCountMax 300

# - Restart ssh service -
sudo systemctl restart ssh
```

## MYSQL

### Installing MYSQL
```bash
sudo mysql_secure_installation      # Press Y anywhere
```

### Creating DB for Django application
```bash
# - Go to shell mysql client -
sudo mysql -u root -p

# - Change <someapp> to your Django app name -
CREATE DATABASE <someapp> DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;

# - Change <password> on yours -
CREATE USER 'django'@'localhost' IDENTIFIED BY '<password>';

# - Change <db_name> , <user> and  <pwd> on yours -
grant all on <db_name>.* to <user>@localhost identified by '<pwd>' with grant option;

FLUSH PRIVILEGES;

# - Fill in mysql client config -
vi website_nordic_walking/server_configs/mysql_django.cnf

# - Content of mysql_django.conf (change data on yours) -
[client]
database = <db_name>
user = <user_name>
password = <password>
host = 127.0.0.1
port = 3306
default-character-set = utf8

# - Generating django secret key -
python3.6 website_nordic_walking/key_gen.py

# - Setting Django ALLOWED_HOSTS
vi /path/to/project/settings/production.py

# - Setting env variables to ~/.bashrc -
# - Example -
export PYTHONPATH=/abs/path/to/project/dir
export DJANGO_SETTINGS_MODULE=<site>.settings.production
export SECRET_KEY='<secret_key>'
export MYSQL_CONF='/abs/path/to/server_configs/mysql_django.cnf'

. ~/.bashrc
source venv/bin/activate

# - Migrations -
python3.6 manage.py makemigrations blog events_calendar gallery static_pages
python3.6 manage.py migrate

# - Deploying static files - 
python3.6 manage.py collectstatic --link

# - Installing require plugins for `ckeditor`
cd /path/to/static/ckeditor/ckeditor/plugins
wget https://download.ckeditor.com/youtube/releases/youtube_2.1.13.zip
unzip youtube_2.1.13.zip
rm youtube_*

# - Creating superuser -
python3.6 manage.py createsuperuser

# # # --- Extra note ---

# - dump data from old DB -
python3.6 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json

# - load data into new db by dump from old db -
python3.6 manage.py db.json
```

## NGINX + UWSGI

### Setting domen name
```
NOTE: add CNAME (with www) and A (with @) 
records into your hosting panel.
```

### NGINX
```bash
deactivate
sudo systemctl enable nginx
sudo vi /etc/sysctl.conf

# - Add next line in the end of the file -
fs.file-max = 40000

sudo sysctl -p
sudo cp website_nordic_walking/server_configs/nginx.conf /etc/nginx/

# - Fill in the nginx.conf -
# - return 301 $sheme://<domain.com>; Change domain on yours in this line -
sudo vi /etc/nginx/nginx.conf

# - Fill in the config file custom_nginx.conf - 
vi website_nordic_walking/server_configs/custom_nginx.conf

sudo cp /path/to/mysite/custom_nginx.conf /etc/nginx/sites-enabled/
sudo nginx -t
```

### Adding SSL
```bash
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install certbot python-certbot-nginx 

sudo certbot --nginx -d <domain.com> certonly
sudo rm /etc/letsencrypt/options-ssl-nginx.conf

crontab -e
# - Add next line for auto updating cert -
@daily certbot renew

# - Uncomment ssl supporting in custom_nginx.conf
```

#### **NOTE**
```
If something was wrong -> reboot your system and try again , in 99 percent of the happenings it helps :D

---> Next fill in the custom_nginx.conf
```

### UWSGI
```bash
sudo python3.6 -m pip install uwsgi

# - Fill in the config file custom_uwsgi.ini -
vi /path/to/custom_uwsgi.ini

# - Copy configs to /etc/...
sudo mkdir -p /etc/uwsgi/vassals
sudo cp /path/to/server_configs/emperor.ini /etc/uwsgi/
sudo ln -s /abs/path/to/server_configs/custom_uwsgi.ini /etc/uwsgi/vassals

sudo systemctl restart nginx.service

# - Running the Django application with uwsgi and nginx -
# - Need for debug , another use systemd -
uwsgi --emperor /etc/uwsgi/emperor.ini

# - UWSGI production -
sudo cp /path/to/server_configs/emperor.uwsgi.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl start emperor.uwsgi.service
sudo systemctl enable emperor.uwsgi.service
```


## Security settings

### Fail2Ban
```bash
sudo apt-get install fail2ban
sudo vi /etc/fail2ban/jail.local

# - Config example -
[ssh]
findtime    = 3600
maxretry    = 6
bantime     = 86400

sudo service fail2ban restart
```
