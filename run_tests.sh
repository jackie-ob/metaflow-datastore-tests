#!/bin/bash
set -e


if [ -z "$STORAGE_BACKEND_TO_TEST" ]; then
	# Hacky, but it will do
	AWS_HOSTNAME_PATTERN='^ip\-'
	if [[ $(hostname) =~ $AWS_HOSTNAME_PATTERN ]]; then
	    STORAGE_BACKEND_TO_TEST=s3
	else
	    set +e
	    curl -H Metadata:true "169.254.169.254/metadata/instance?api-version=2017-08-01" >/dev/null 2>&1
	    if [ "$?" -eq 0 ]; then
		STORAGE_BACKEND_TO_TEST=azure
	    else
		echo "Could not determine storage backend to test!"
		echo "You can also set STORAGE_BACKEND_TO_TEST manually in env"
		exit 1
	    fi
	    set -e
	fi
fi

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
    for ds in local "$STORAGE_BACKEND_TO_TEST"
    do
        echo -n "$testbase $ds"
        METAFLOW_DATASTORE=$ds $test $1 $1
        base="logs/$testbase.$ds"
        echo " $(cat $base.$first.timing)"
    done
done
