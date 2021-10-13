# sendika-server

The backend side of the sendika web application


## First thing to do 

1. Installing the pipenv module in python
```
pip install pipenv
``` 
2. Install all the modules in the pip file 
```
pipenv install
```
3. Open the virtual environment (**Make sure already inside sendika-server folder**)
```
pipenv shell
```    
4. To run the django server 
```
python manage.py runserver
```

### Extra note
After make update to the model or database 
```
python manage.py makemigrations
python manage.py migrate
```



# Resources
* Good example of using Django as backend and React as front-end 
https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react


* Deploying AI model using Django with React
https://www.aionlinecourse.com/blog/deploy-machine-learning-model-using-django-and-rest-api


* Good introduction to Redux in React (To the point)
https://www.youtube.com/watch?v=CVpUuw9XSjY


* Reference in integrating Backend to React
https://www.youtube.com/watch?v=ngc9gnGgUdA
