export METAFLOW_DATASTORE_SYSROOT_S3=s3://jackie-scratch-s3-test/datastore_test_20210625
export METAFLOW_ARTIFACT_LOCALROOT=/mnt/metaflow-tmp
export METAFLOW_CLIENT_CACHE_PATH=/mnt/metaflow_client
export METAFLOW_DATASTORE_SYSROOT_LOCAL=/mnt/.metaflow

rm -rf $METAFLOW_ARTIFACT_LOCALROOT $METAFLOW_CLIENT_CACHE_PATH $METAFLOW_DATASTORE_SYSROOT_LOCAL
mkdir -p $METAFLOW_ARTIFACT_LOCALROOT

time ./run_tests.sh ../metaflow $1 > aws_datastore_results.csv 2>aws_datastore_results.err
