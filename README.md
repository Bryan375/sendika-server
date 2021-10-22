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

# Dependencies
## .whl files
To run the model, please go to [this link](https://www.lfd.uci.edu/~gohlke/pythonlibs/). Download these libraries with the code of **cp37** :
* matplotlib
* numpy
* pandas
* scikit-learn
* scipy
* tensorflow
* pytorch

You can place the files anywhere you like but it is recommended to put them inside of the ```sendika-server/sendika-server``` directory.
You can install them by using: `pip install <fileName>` while accessing the pipenv.

## Deepchem
1. Please clone [Deepchem](https://github.com/deepchem/deepchem.git) from their repository.
2. `cd` into the `scripts` folder of Deepchem and run `install_deepchem_conda.sh 3.7 gpu`
3. run `conda activate deepchem`
4. Back to ```/Deepchem/``` and run `python setup.py install`

## pip install
1. After tensorflow was installed, run `pip install --upgrade tensorflow`
2. run `pip install rdkit-pypi`

# Resources
* Good example of using Django as backend and React as front-end 
https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react


* Deploying AI model using Django with React
https://www.aionlinecourse.com/blog/deploy-machine-learning-model-using-django-and-rest-api


* Good introduction to Redux in React (To the point)
https://www.youtube.com/watch?v=CVpUuw9XSjY


* Reference in integrating Backend to React
https://www.youtube.com/watch?v=ngc9gnGgUdA
