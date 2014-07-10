china-voice
===========


Prepare
-------

```Bash
$ npm install -g bower gulp
$ virtualenv venv --python=python2.7
```


Build
-------

```Bash
$ pip install -r requirements.txt
$ npm install
$ bower install
$ gulp
```


Debug
-----

```Bash
$ make port=PORT
```


Deploy
------

```Bash
# start server
$ make start-uwsgi port=PORT

# reload uwsgi
$ make reload-uwsgi

# stop uwsgi
$ make stop-uwsgi
```