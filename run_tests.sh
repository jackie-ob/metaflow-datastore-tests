#!/bin/bash
set -e

rm -Rf logs/*
mkdir -p logs 

first=$(basename $1)
second=$(basename $2)
echo "test datastore time:$first peakmem:$first time:$second peakmem:$second"
for test in tests/*
do
    testbase=$(basename $test)
    if [ -n "$3" ] && [ "$3" != "$testbase" ]
    then
        continue
    fi
    for ds in local s3
    do
        echo -n "$testbase $ds"
        METAFLOW_DATASTORE=$ds $test $1 $2
        METAFLOW_DATASTORE=$ds $test $2 $1
        base="logs/$testbase.$ds"
        echo " $(cat $base.$first.timing) $(cat $base.$second.timing)"
    done
done
