Set up:

```bash
$ sudo apt-get install python3-venv
$ git clone https://github.com/replaceafill/flask-i18n.git
$ cd flask-i18n
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ pybabel compile -d app/translations
$ python runserver.py
```

Open http://0.0.0.0:5000 in your web browser.
