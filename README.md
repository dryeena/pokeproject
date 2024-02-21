# pokeproject
Popular Poke Project is a project that uses reddit to gather and manipulate data for pokemon; and is useful for finding which ones have been the most popular in that given day


## Get Started
Please install the following to get started
Docker and docker compose: https://docs.docker.com/compose/install/
Python 3.10 or higher: 

### To run all quickly
```docker compose -f docker-compose-full.yml up```

This allows you to view the webapp on `localhost:8000`

As well as the grafana on `localhost:3000` with username and password of `admin`

### To install requirements run
```python3 -m venv venv && source venv/bin/activate```  
```pip3 install -r requirements.txt```

### To load the environment
```source venv/bin/activate```
```docker compose up```

### To run tests run
```docker compose up```

In a seperate window

```python3 -m unittest discover src/test```

### To load application run in seperate windows
```python3 -m src.apps.gatherer```

```python3 -m src.apps.processor```

```python3 -m src.apps.app```