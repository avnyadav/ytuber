### Installing PostgreSQL in Ubuntu 20.04

Log into your Ubuntu system and update the system software packages using the following apt command.

```
sudo apt update
```
Now install the latest version of PostgreSQL from the default Ubuntu repositories.
```
sudo apt install postgresql
```
During the installation, the installer will create a new PostgreSQL cluster (a collection of databases that will be managed by a single server instance), thus initialize the database. The default data directory is /var/lib/postgresql/12/main and the configurations files are stored in the /etc/postgresql/12/main directory.

After PostgreSQL installed, you can confirm that the PostgreSQL service is active, running and is enabled under systemd using the following systemctl commands:

```
sudo systemctl is-active postgresql
```
```
sudo systemctl is-enabled postgresql
```
```
sudo systemctl status postgresql
```
Also, confirm that the Postgresql server is ready to accept connections from clients as follows:
```
sudo pg_isready
```

### Creating Database in PostgreSQL
To create a new database in PostgreSQL, you need to access the PostgreSQL database shell (psql) program. First, switch to the postgres system user account and run the psql command as follows:

```
sudo su - postgres
```

```
psql
```
Launch sql command line
```
CREATE USER <user_name> WITH PASSWORD '<password>';
```
Create database using below command.
```
CREATE DATABASE <database_name>;
```
Grant  all permission on database for an user 
```
GRANT ALL PRIVILEGES ON DATABASE <database_name> to <user_name>;
```

### Configuring PostgreSQL Client Authentication
PostgreSQL uses client authentication to decide which user accounts can connect to which databases from which hosts and this is controlled by settings in the client authentication configuration file, which on Ubuntu is located at /etc/postgresql/12/main/pg_hba.conf.

Open this file using your favorite text editor as shown.
```
sudo vim /etc/postgresql/12/main/pg_hba.conf
```

### Installing pgAdmin4 in Ubuntu
pgAdmin4 is not available in the Ubuntu repositories. We need to install it from the pgAdmin4 APT repository. Start by setting up the repository. Add the public key for the repository and create the repository configuration file.

```
curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add
```

```
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
```
Then install pgAdmin4.
```
sudo apt install pgadmin4
```

The above command will install numerous required packages including Apache2 webserver to serve the pgadmin4-web application in web mode.

Once the installation is complete, run the web setup script which ships with the pgdmin4 binary package, to configure the system to run in web mode. You will be prompted to create a pgAdmin4 login email and password as shown in the screenshot below.

This script will configure Apache2 to serve the pgAdmin4 web application which involves enabling the WSGI module and configuring the pgAdmin application to mount at pgadmin4 on the webserver so you can access it at:


to launch postgres sql browser
```
sudo /usr/pgadmin4/bin/setup-web.sh 
```

To release occupied port in linux system.
```
sudo fuser -k 8000/tcp
```

### Serving static files
```
python manage.py collectstatic
```

### Creating app in Django
```
python manage.py startapp <app_name>
```


### ckeditor

```
pip install ckeditor
```

To run project with https use below module
```
pip install django-sslserver
```

add enty to INSTALLED_APPS in root settings.py file "sslserver"

Launch Django app using below command
```
python manage.py runsslserver localhost:8000
```

To create database diagram

Install a diagram
```
sudo apt install python-pygraphviz
```

Now in your python environment (maybe some virtual environment)
```
pip install django-extensions pygraphviz
```

```
python manage.py graph_models -a -g -o imagefile_name.png
```

<iframe width="424" height="238" src="" title="How I started speaking English without fear (as a non-native speaker)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>




Description
Helping people to learn DevOps topics easily 💙

I create new videos every second week, topics include mainly DevOps tutorials. Subscribe and activate bell notification so you don't miss new videos :)

I'm a Docker Captain, AWS Container Hero & CNCF Ambassador 🤓  💪

►  https://www.techworld-with-nana.com/

Tutorials so far
 - Docker
 - Kubernetes
 - Jenkins
 - Python
 - Ansible
 - Prometheus Monitoring
 - Terraform
 - YAML
 - & more!

Have fun watching my videos! 🙂