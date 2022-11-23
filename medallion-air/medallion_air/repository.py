import os

from dagster import repository, with_resources

from .assets import bronze_layer_assets, gold_layer_assets, silver_layer_assets
from .jobs.air_quality import all_air_assets_job
from .resources import resource_defs_by_env
from .schedules.air_quality import (
    hourly_all_assets_schedule,
    partitioned_all_assets_schedule,
)

all_assets = [*bronze_layer_assets, *silver_layer_assets, *gold_layer_assets]
all_jobs = [all_air_assets_job]


@repository
def medallion_air():
    deploy_env = os.environ.get("MEDALLION_AIR_ENV", "dev")
    resource_defs = resource_defs_by_env[deploy_env]
    asset_defs = [with_resources(all_assets, resource_defs=resource_defs), *all_jobs]
    schedules = [partitioned_all_assets_schedule, hourly_all_assets_schedule]

    return asset_defs + schedules
