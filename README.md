# MamiUX - A Simple Visual A/B Testing Tool

We use this tool internally to conduct quantitative research using visual A / B testing method. This tool is not made to replace other paid tools that are more complete and sophisticated, but to help us do A / B testing quickly and easily. Please feel free to use and improve it!

~ Keep scrolling for `How to Setup`

## 0. Screenshots
![Screenshot 1](https://i.postimg.cc/vTYdKkr5/Web-1366-1.png)
![Screenshot 2](https://i.postimg.cc/J4hL5w4L/Web-1366-2.png)
![Screenshot 3](https://i.postimg.cc/15YZWWfN/Web-1366-3.png)
![Screenshot 4](https://i.postimg.cc/Hkq1mV0Y/Web-1366-4.png)
![Screenshot 5](https://i.postimg.cc/2y0fNGGM/Web-1366-5.png)
![Screenshot 6](https://i.postimg.cc/YCGBT1WD/Web-1366-6.png)


## 1. Setting Up Project

#### In this project we need to install requirements for machine:
-	Postgresql/Mysql 
-	Python > 3.7
-	Django >= 3.0


### 2. Install requirements.txt 
cd to main project directory, and run command:

` $ pip install requirements.txt `

### 3. Setting Environment Database
Open file `config/<environment>/settings.py` and find Variable `DATABASES`

##### - For Postgresql
```

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', 
        'NAME': 'YOUR_DATABASE_NAME',
        'USER': 'YOUR_DATABASE_USER',
        'PASSWORD': 'YOUR_DATABASE_PASSWORD'
    }
}

```
##### - For Sqlite :

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

### 4. Migrate Database
`$ ./manage.py migrate`

### 5. Create Superuser
`$ ./manage.py createsuperuser `

### 7. Running server
`$./manage.py runserver`


## 2. Future Plan (Or I hope so...)
- Add User Personas feature
- Add Project Brief feature


## API Docs

Postman collection : [https://www.getpostman.com/collections/](https://www.getpostman.com/collections/d6097a098c8f4d2ef071)





