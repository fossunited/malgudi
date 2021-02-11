# Malgudi - the learning platform of FOSS United

Malgudi is the learning platform of FOSS United that provides courses for learning programming.

The system is very early stages of implementation and lot of things are likely to change as we experiment with various ideas and see their effectiveness.

## How to run

Step 1: Clone the repo.

```
$ git clone git@github.com/fossunited/malgudi
```

Step 2: Setup a virtualenv and install the dependencies.

```
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

Step 3: Create a database.

```
$ createdb malgudi
```

Step 4: Run the development server.

```
$ export FLASK_DEBUG=1
$ python run.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```