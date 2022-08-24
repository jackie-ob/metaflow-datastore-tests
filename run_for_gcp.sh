export METAFLOW_DATASTORE_SYSROOT_GCP=gs://ob_gcp_exploration/benchmark/$(date +%s)
export METAFLOW_ARTIFACT_LOCALROOT=/mnt/metaflow-tmp
export METAFLOW_CLIENT_CACHE_PATH=/mnt/metaflow_client
export METAFLOW_DATASTORE_SYSROOT_LOCAL=/mnt/.metaflow

# export GOOGLE_APPLICATION_CREDENTIALS=~/.config/gcloud/application_default_credentials.json
rm -rf $METAFLOW_ARTIFACT_LOCALROOT $METAFLOW_CLIENT_CACHE_PATH $METAFLOW_DATASTORE_SYSROOT_LOCAL
mkdir -p $METAFLOW_ARTIFACT_LOCALROOT

time ./run_tests.sh ../metaflow $1 > gcp_results.csv 2>gcp_datastore_results.err
