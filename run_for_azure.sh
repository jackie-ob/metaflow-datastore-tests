export METAFLOW_DATASTORE_SYSROOT_AZURE=test-azure-storage/datastore-bench
export METAFLOW_AZURE_STORAGE_ACCOUNT_URL=https://obbenchmark1.blob.core.windows.net/
export METAFLOW_ARTIFACT_LOCALROOT=/mnt/metaflow-tmp
export METAFLOW_CLIENT_CACHE_PATH=/mnt/metaflow_client
export METAFLOW_DATASTORE_SYSROOT_LOCAL=/mnt/.metaflow

export METAFLOW_AZURE_STORAGE_ACCESS_KEY=blah

mkdir -p $METAFLOW_ARTIFACT_LOCALROOT
time ./run_tests.sh ../metaflow noop > azure_datastore_results.csv 2>azure_datastore_results.err
