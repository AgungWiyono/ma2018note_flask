# ma2018note_flask
The apps for sharing notes with others, or use it for yourself. We will add chat feature in future.

The project is sub-app from Muslim Apps Project

## Prequisites
Make sure you have `python3` with `pipenv` installed, or `python3` with `venv`(usually `python3` has been installed with `venv`.

1. **Setting up `pipenv`**
    1. If `pip` hasn't been installed, install it:
    
         ```
         $ sudo apt-get install python3-pip
         ```
    
    1. Install `pipenv` with pip
    
        ```
        $ python3 -m pip install pipenv
        ```
    
    1. 'pipenv` has been installed on your computer.
        Go to project directory
        
        ```
        $ pipenv install
        ```

1. **Setting up `venv`.**
    1. Go to project directory and create virtual environment
    
        ```
        $ python3 -m venv env
        ```
        
    1. Activate virtual environment and install required packages

        `$ source env/bin/activate`
        
        `$ pip install -r requirements.txt`

## Activate environment
First, go to project directory.

If you use `pipenv`:
    ```
    $ pipenv shell
    ```

Otherwise, if you use `venv`:
    ```
    $ source env/bin/activate
    ```

## Deactivate environment
If you use `pipenv`:

`$ exit`


If you use `venv`:

`$ deactivate`

## How to run
After environment has been activated, export `SECRET_KEY`. The value could be anything. After that, run `flask`.

```
$ export SECRET_KEY='secret-key'
$ flask run
```

## API Swagger Documentation
After you run `flask` in 'How to run' section open `127.0.0.1:5000/api` in your browser to see swagger documentation.

## Admin CRUD interface
To insert data, you could do it with admin interface on `127.0.0.1:5000/admin`.

## Contributing
If you find any bug or have advice, feel free to open an issue.