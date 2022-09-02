
# Introduction

The goal of this project is to provide a backend for lactachain project. This backend is developed with Django framework.


### Main features

* Manage farms

* Manage transports

* Manage silos

# Usage


This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django

After that just install the local dependencies, run migrations, and start the server.
      

# Lactachain

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@ggithub.com/borjasueiro/lactachain-backend
    $ cd lactachain-backend
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver