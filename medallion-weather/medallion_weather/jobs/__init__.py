from dagster import AssetSelection, define_asset_job

from ..assets import ALL_ASSET_GROUPS
from ..assets.partitions import hourly_partitions_def

DAGSTER_K8S_CONFIG_TAGS = {
    "dagster-k8s/config": {
        "container_config": {
            "resources": {
                "requests": {"cpu": "500m", "memory": "1Gi"},
                "limits": {"cpu": "1000m", "memory": "2Gi"},
            }
        }
    }
}

all_assets_job = define_asset_job(
    name="all_assets_job",
    selection=AssetSelection.groups(*ALL_ASSET_GROUPS),
    description="This job tries to materialize all asset groups.",
    tags=DAGSTER_K8S_CONFIG_TAGS,
    partitions_def=hourly_partitions_def,
)
