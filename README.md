Techblog: A blog with the purpose of helping in-house dev team for reducing google effort for small things.
==================

Blog developed in django with the simple but elegant design.

* CSS and Latex fonts integrated
* Posts are presented in very efficient and readable manner
* Formulas can be added with Latex notation 
* Share in social networks
* RSS feed
* Post search with tags and auto suggest
* Blog optimized for SEO
* Comments with disqus integration
* Easy writing with Ckeditor (including easy file and image upload)
* Responsive for mobile


Installation
==================

To start with project just follow the few steps 

	$ git clone https://github.com/keyurr2/tech-blog-portal.git
	$ cd tech-blog-portal
	$ pip install -r requirements.txt 

NOTE: Django version must be 1.7 and Python has to be version 2.7.

Set up the project in localhost
==================================================
The first step is to generate the database. In the projects folder:
  
  	$ cd tech-blog-portal
	$ python manage.py syncdb  
	
Django will ask you to create a superuser. You have to put the username and password. The email is optional. 
This will generate a file called `db.sqlite3` which is the database where all the blog content is stored.

After that you have to make what is called a migration, to create the tables in your database. To do that:
	
	$ python manage.py makemigrations
	$ python manage.py migrate
