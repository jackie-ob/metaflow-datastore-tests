#!/bin/bash
set -e

rm -Rf logs/*
mkdir -p logs 

first=$(basename $1)
echo "test datastore time:$first peakmem:$first"
for test in tests/*
do
    testbase=$(basename $test)
    if [ -n "$2" ] && [ "$2" != "$testbase" ]
    then
        continue
    fi
    for ds in azure local
    do
        echo -n "$testbase $ds"
        METAFLOW_DATASTORE=$ds $test $1 $1
        base="logs/$testbase.$ds"
        echo " $(cat $base.$first.timing)"
    done
done
