## Start Commands

### Requirements

```
$ pip install -r requirements.txt
```

### Super User

```
$ python manage.py createsuperuser
```

## Social Authentication

The app has the option to social authentication.

### Hosts File

Find and edit your machine's hosts file:

```
127.0.0.1 mysite.com
```

> - **Windows path:** C:\Windows\System32\Drivers\etc\hosts
> - **Linux and macOS path:** /etc/hosts

### Runserver

Use my self-signed certificate and use the command:

```
$ python manage.py runserver_plus --cert-file cert.crt
```

> Recommended to use Mozilla Firefox

## Main paths

- admin/
- account/ (bookmarklet script location)
- social-auth/
- images/
