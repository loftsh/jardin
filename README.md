Jardin
======

[![Build Status](https://travis-ci.com/loftsh/jardin.svg?branch=master)](https://travis-ci.com/loftsh/jardin)

Jardin is a simple Django app to monitor and trigger event in our
IoT-connected-smart-8.0-bigdata-machinelearning-stupidAdjectives-garden.

- Aquaponie module handle our aquaponics farm with fish tank and
  culture monitoring and water cycle actions
- Jardin hanle plants hygrometrics monitoring and sprinkling
 

## Set up the development environment

You can use the included dockerfile to setup a dev environment:
```
make up
make logs
```

And browse to 127.0.0.1:8000/


## Test suite

The project has a simple test suite:

```
make test
```

Please make sure that every test pass before pushing any pull request.


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
