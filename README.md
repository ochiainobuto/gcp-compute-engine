# gcp-compute-engine  

sudo apt-get -y install git python-pip python-dev python-flask python-wtforms python-arrow python-flask-sqlalchemy python-pymysql python-flaskext.wtf  

sudo pip install --upgrade setuptools  
sudo pip install --upgrade gcloud  
git clone https://github.com/ochiainobuto/gcp-compute-engine  
cd gcp-compute-engine  
sudo app_v1/install.sh  

sudo systemctl enable dengonban.service  
sudo systemctl start dengonban.service  
sudo systemctl status dengonban.service  
sudo systemctl restart dengonban.service

path_w = './test/test_w.txt'

s = 'New filw'

with open(path_w, mode = 'w') as f:
	f.write(s)

with open(path_w) as f:
	print f.read()
