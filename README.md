
# Datastore test suite for Metaflow

Usage:

0. Clone this repo
```
git clone http://github.com/tuulos/metaflow-datastore-tests
```

1. Install dependencies of Metaflow
```
python3 -m pip install click requests boto3 pylint
```

2. Clone Metaflow `master`
```
git clone http://github.com/Netflix/metaflow
```

3. Clone another branch for comparison, e.g. `convergence`
```
git clone --branch convergence http://github.com/Netflix/metaflow metaflow-cc
```

3. Run tests (this is going to take more than an hour, so consider using `screen`):
```
cd metaflow-datastore-tests
time ./run_tests.sh ../metaflow ../metaflow-cc/ > results.csv
```

Optionally, you can run a single test, e.g. `noop`, by specifying its name:
```
./run_tests.sh ../metaflow ../metaflow-cc/ noop > results.csv
```
