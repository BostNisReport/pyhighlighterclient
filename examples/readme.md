# pyhighlighterclient examples
**pyhighlighterclient** is a demo silverpond client library. Not published on PyPi yet. so should be need to install in development mode.


## setup the environment file(.env).

- 3 parameters in .env file

```
GRAPHQL_API_TOKEN=c5c37a60fed25025f6501.....
GRAPHQL_API_ENDPOINT=https://staging.high.....
PRESIGNED_GET_URL=https://staging.highli....
```

- if you don't want use .env file, should be need pass the api token and api endpoint, presigned url parameters in class instruction.
```
from pyhighlighterclient import Experiments, ExperimentComment

experiments = Experiments(apitoken='c5c37a60fe...', apiurl='https://staging.highlig...')
experimentcomment = ExperimentComment(apitoken='c5c37a60fe...', apiurl='https://staging.highlig...', presignedurl='https://staging.high...')
```

## examples
- See a detail example [experiments](examples/example_experiments.py).
- See a detail example [researchplans](examples/example_researchplans.py).