set -e

function runmf()
{
    N=1
    logbase="logs/$2.$METAFLOW_DATASTORE.$(basename $1)"
    rm -f timing
    for ((i=0;i<$N;i++))
    do
        export PYTHONPATH=$1
        log="$logbase.$i"
        /usr/bin/time -f '%e %M' -a -o timing python3 flows/$2.py --no-pylint $3 $4 $5 > $log.out 2> $log.err
    done
    took=$(awk "{ x += \$1; m += \$2 } END { print x / $N \" \" int(m * 1000. / $N) }" < timing)
    echo -n "$took" > $logbase.timing
    rm -f timing
}
