# Django Custom User
This is a custom user model that uses email to authenticate.

# Installation
1. Clone this github repo.

2. Add `authentication` to `INSTALLED_APPS` in `settings.py`

```
INSTALLED_APPS = [
    ...
    'authentication',
]
```

3. Change the `AUTH_USER_MODEL` in `settings.py`

```
AUTH_USER_MODEL = 'authentication.User'
```

4. Make migrations
```
python manage.py makemigrations
```

5. Migrate
```
python manage.py migrate
```

That's all! You can use the new user model.