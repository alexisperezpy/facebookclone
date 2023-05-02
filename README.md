# Peoplebook
Facebook clone made using python and Django.
Hello there, if you want to clone my project here are the steps to clone it on your local machine.
Sample images of the project are available in sample_images folder.

Clone the project
Use this command to clone the project.

git clone https://github.com/alexisperezpy/facebookclone.git

Setting up virtual environment
To setup virtual enviroment you need to follow steps based on your OS. Also make sure you are in the project directory.

For windows
Open windows powershell as administrator and run these commands.

python -m venv myvenv
myvenv\Scripts\activate

For mac-os/linux
Open terminal and run these commands.

python3 -m venv myvenv
myvenv/bin/activate

You will know that you have virtualenv started when you see that the prompt in your console is prefixed with (myvenv).

Installing requirements
To install requirements related to this project run this command.

pip install -r requirements.txt

Run the server
To run the server use this command.

python manage.py runserver

Drop a star if you like it.
