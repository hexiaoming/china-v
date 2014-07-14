china-voice
===========


Prepare
-------

```Bash
# need bower gulp & virtualenv
$ npm install -g bower gulp
$ virtualenv venv --python=python2.7

# install dependencies
$ pip install -r requirements.txt
$ npm install
$ bower instal
$ pip install xlrd
```


Build
-------

```Bash
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
