# Toratora

Streaming Anime Free

## Styling and UI
- Tailwindcss
- Preline UI

## Settings
### Databases Postgresql
https://neon.tech/

## Installations
### Install 
```
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py tailwind install
```

### Start Server
#### For Tailwind Development
```
python manage.py tailwind start
```
#### For Django
```
python manage.py runserver
```