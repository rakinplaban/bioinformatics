# Distinctiveness and Complexity
1. The whole application is based on single page. The full operation is done with javascript. 
2. Popup forms.
3. Auto complete search bar with jQuery.

# What contains my each file
`forms.py` contains django modelform. <br>
`urls.py` contains routings.<br>
`register.html` and `login.html` have authentication code. <br>
`layout.html` has linked css and js files to html.<br>
`index.html` has the entire operational front-end.<br>
`action.js` has the **javascript** controling the front-end and `style.scss` contains the styling.

# To run my application, the following commands should be run
1. Create a virtual environment <br>
`python3 -m venv venv`
2. Activate the environment<br>
`venv\Scripts\activate`
3. Install packages on the environment with<br>
`pip install -r requirements.txt`
4. Migrate using followings: <br>
`python manage.py makemigrations bioinformatics`<br>
`python manage.py migrate`
5. Finally run the server using<br>
`python manage.py runserver`