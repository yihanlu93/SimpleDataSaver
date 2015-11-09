# SimpleDataSaver

Vagrant Base Box: <a href="https://atlas.hashicorp.com/boxes/search?utm_source=vagrantcloud.com&vagrantcloud=1">hashicorp/precise32 (virtualbox, 1.0.0)</a><br>
Web framework provider: <a href="https://www.djangoproject.com/">Django</a><br>
Database:<a href="https://www.mysql.com/">MySQL</a><br>
Backend Language: <a href="https://www.python.org/">Python 2.7</a><br>

This is a simple data saver on vagrant, which saves following infomations to a database:
- name (text)
- sex (select: male|female)
- age (number)
- active (select: yes|no)
- tags (text)

<h3>To run this project:</h3><br>
1. vagrant up<br>
2. vagrant ssh<br>
3. sudo python /srv/website/server/FirstBlog/manage.py runserver 0.0.0.0:66 <br>
[type this in command-line to start the server at virtual box localhost at port 66]<br>
4. Access the SimpleDataSaver from your host web browser at "55.55.55.5:66"<br>

<h3>To run unit test:</h3><br>
In the vagrant, type "python /srv/website/server/FirstBlog/manage.py test"<br>
[the unit test is powerd by Django]<br>
