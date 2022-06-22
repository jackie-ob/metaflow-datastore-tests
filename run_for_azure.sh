export METAFLOW_DATASTORE_SYSROOT_AZURE=test-azure-storage/datastore-bench
export METAFLOW_AZURE_STORAGE_ACCOUNT_URL=https://obbenchmark1.blob.core.windows.net/

time ./run_tests.sh ../metaflow big_pickle > azure_datastore_results.csv 2>azure_datastore_results.err
