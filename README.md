activate your virtual env in root of this project using pipenv shell

pip install django pillow

pip install opencv-python opencv-contrib-python

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

##### for linux

sudo apt-get install -y build-essential cmake unzip pkg-config

sudo apt-get install -y libjpeg-dev libpng-dev libtiff-dev

sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev

sudo apt-get install -y libatlas-base-dev gfortran



running project

python manage.py runserver

![architecture](arch.jpg)
