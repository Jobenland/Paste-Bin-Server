# Paste Bin Server

##### Version: 1.0.0

## Author
[Jonathan Obenland](https://jonathanobenland.com)

## About

I always struggled getting links from my phone to other computers and was frusturated dealing with overly complex systems for such a simple idea

## How-To

Users can navigate to the website and enter any text they may want to send. Users will then add a key to the text that will be able to grab the text from another computer. Users can then navigate to the retrieve text option, enter their key, and copy the text.

### Create a virtual environment

```bash
pyenv virtualenv venv
pyenv activate venv
pip install -r requirements.txt
```

### Run

```bash
python manage.py runserver
python manage.py runserver --host=<enter IP>
```

## Credits
Thanks to 
1. [Daniel Abeles](https://twitter.com/Daniel_Abeles)
for other help
