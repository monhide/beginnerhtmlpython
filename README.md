	Part 1
		# set up developement environment
			# check conda installed
				MacBook-Pro:~ username$ conda --version
			# create new environment
				MacBook-Pro:~ username$ conda create --name basic-env python=3.7
				MacBook-Pro:~ username$ y
			# launch environment
				MacBook-Pro:~ username$ source activate basic-env
			# install django to that environment
				(basic) MacBook-Pro:~ username$ pip install Django==2.0.7
			# check django installed
				(basic-env) MacBook-Pro:~ username$ python -m django --version
		# set up the django project
			# create project
				(basic-env) MacBook-Pro:~ username$ django-admin startproject basicProject
			# launch the development server to check
				(basic-env) MacBook-Pro:~ username$ cd basicProject
				(basic-env) MacBook-Pro:basicProject username$ python manage.py runserver
				# can check at: http://127.0.0.1:8000/
				cmd + c to quit
			# create an app (subset of website)
				(basic-env) MacBook-Pro:basicProject username$ python manage.py startapp basicApp
			# write some views using
				 	basicApp/views.py
					basicApp/urls.py
					basicSite/urls.py
					# can check at: http://127.0.0.1:8000/basicApp/

	Part 2
		Adding Model
			edited 	basicApp/models.py
		Activating Models
			(basic-env) MacBook-Pro:basicProject username$ python manage.py migrate
			(basic-env) MacBook-Pro:basicProject username$ python manage.py makemigrions
		Adding Django admin
			(basic-env) MacBook-Pro:basicProject username$ python manage.py createsuperuser
			(basic-env) MacBook-Pro:basicProject username$ monica
			(basic-env) MacBook-Pro:basicProject username$ monica@email.com
			(basic-env) MacBook-Pro:basicProject username$ password1234
		Check on:
			(basic-env) MacBook-Pro:basicProject username$ python manage.py runserver
			http://127.0.0.1:8000/admin/
			edited	basicApp/admin.py to add in models
			
