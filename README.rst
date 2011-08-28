PowerDNS Example Project
========================

The 'example' directory contains a ready made Django project that should "just work" in the same way
that any standard Django app does.

Firsly, create the database and admin user::

  	user@machine:~/django-freeradius/example> ./manage.py syncdb
	Creating table auth_permission
	Creating table auth_group_permissions
	Creating table auth_group
	Creating table auth_user_user_permissions
	Creating table auth_user_groups
	Creating table auth_user
	Creating table auth_message
	Creating table django_content_type
	Creating table django_session
	Creating table django_site
	Creating table django_admin_log
	Creating table realmgroup
	Creating table realms
	Creating table attributelist
	Creating table nas
	Creating table radpostauth
	Creating table radreply
	Creating table radusergroup
	Creating table radcheck
	Creating table radgroupcheck
	Creating table radgroupreply
	Creating table radippool
	Creating table radacct

	You just installed Django's auth system, which means you don't have any superusers defined.
	Would you like to create one now? (yes/no): yes
	Username (Leave blank to use 'user'):
	E-mail address: user@domain.com
	Username (Leave blank to use 'root'): peter
	E-mail address: peter.nixon@vodafone.com
	Password: 
	Password (again): 
	Superuser created successfully.
	Installing index for auth.Permission model
	Installing index for auth.Group_permissions model
	Installing index for auth.User_user_permissions model
	Installing index for auth.User_groups model
	Installing index for auth.Message model
	Installing index for admin.LogEntry model
	No fixtures found.


Secondly, run the development web server::

  user@machine:~/django-freeradius/example> ./manage.py runserver
  Validating models...
  0 errors found

  Django version 1.1.1, using settings 'example.settings'
  Development server is running at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.

Thirdly, navigate to http://127.0.0.1:8000/admin/ with your favourite web browser.
