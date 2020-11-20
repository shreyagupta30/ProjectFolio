## Installation and Setup

### Prerequisites
- You should have NodeJS installed (12.x or above)
- pipenv should be installed in the system. It can be done using `sudo pip3 install pipenv`.
- Change the version of the python in `Pipfile` according to the python version available in your system


### Setup and running of project (Frontend + Backend)

- Fork the repo and clone it.
- Navigate to the cloned repo.
- Activate env using `pipenv shell` and install dependencies by `pipenv install`
- Install all react dependencies by running `yarn install`
- Run `build_local.sh`. (Make sure it's in executable mode by `sudo chmod +x build_local.sh`)
- Start the backend server
  `python ./manage.py runserver`
  
**This runs the backend server at default port `8000`.
  Open [http://localhost:8000](http://localhost:8000) to view it in the browser.**<br />

### Setup and running of project (Only Frontend)

- At your root directory run `yarn install` to install all the dependencies
- To start react dev server `yarn start`

This runs the app in the development mode.
**Open [http://localhost:3000](http://localhost:3000) to view it in the browser.**

The page will reload if you make edits.

## Production grade deployment
This project tried to follow the best practices and you can directly deploy the repo with the following points -

- Create an .env in your deployment environment(refer .env.example file for the same).
    - For django `SECRET_KEY` you can generate one from [here](https://djecrety.ir/)
    - Set DEBUG = 'False' when using in production/live deployment.
- Add the hostname/url(the one on which your deployed server is working) in the `settings.py` file (under allowed hosts array)
- Add your suitable `TIME_ZONE` and `LANGUAGE_CODE` in `settings.py` according to your zone and locale.

#### Note [Important]

- The `manage.py` file is moved out of the default django project. So everytime you run `manage.py startapp app`, it will create the required app in the root of the project. So you will have to move it in the backend folder and while registering the app in `settings.py`, you will have to mention `backend.app`.
- The `config` folder in the backend directory is the actual root project of the django project (one which has django settings and main app urls).
- There is a folder named `demo` in the backend folder. That's a demo api folder for reference.
- This project has pre-commit. So if you are using this project on which a lot of people are contributing, make sure you run `pre-commit install` in the project repo so that git hooks are enabled.
- Stuff you can delete (I added them just to refer)
    - `index.js` and related files in `./src/` and `app.js` and related files in `./src/components/`
    - `demo` folder from `./backend/` 

