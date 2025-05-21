# Commands for babel
```commandline
$ pybabel extract -o translations/messages.pot src/handlers/*.py
$ pybabel init -i translations/messages.pot -d translations/ -l ru
$ pybabel init -i translations/messages.pot -d translations/ -l en
$ pybabel compile -d translations
```