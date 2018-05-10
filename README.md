Jardin
======

Jardin is a simple Django app to monitor and trigger event in our
IoT-connected-smart-8.0-otherStupidAdjectives-garden.

- Aquaponie module handle our aquaponics farm with fish tank and
  culture monitoring and water cycle actions
- Jardin hanle plants hygrometrics monitoring and sprinkling
 

## Set up the development environment

You can use Vagrant to setup a VM with our dev env:
```
vagrant up
vagrant ssh
cd /code
```

Then just run Django's migrations and run the server:

```
python3 manage.py migrate
python3 manage.py runserver 127.0.0.1:8080
```

And browse to 127.0.0.1:8081/


## TODO

- Make an abstract layer above pigpio to handle the dev env (where we
  don't have it) / handle other library / handle pigpio failures
- Improve global aesthetics
- Combine in the dashboard every information of the aquaponic system:
 - Water level graph
 - Temperature graph
 - Visualisation of pump state
 - Actions to trigger the start or the stop of a pump
- Write the form to create ebbs
- Handle the modification of ebbs