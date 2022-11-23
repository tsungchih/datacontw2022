import os

from dagster import repository, with_resources

from .assets import (
    bronze_layer_assets,
    external_source_assets,
    gold_layer_assets,
    silver_layer_assets,
)
from .jobs import all_assets_job
from .resources import resource_defs_by_env
from .sensors.asset_sensors import from_air_gold_aqi_with_pm_asset

# external_assets = [*external_source_assets]
all_assets = [
    *bronze_layer_assets,
    *silver_layer_assets,
    *gold_layer_assets,
    *external_source_assets,
]
all_jobs = [all_assets_job]
all_sensors = [from_air_gold_aqi_with_pm_asset]


@repository
def medallion_weather():
    deploy_env = os.environ.get("MEDALLION_WEATHER_ENV", "dev")
    resource_defs = resource_defs_by_env[deploy_env]
    asset_defs = [
        with_resources(all_assets, resource_defs=resource_defs),
        *all_jobs,
        # *external_assets,
    ]

    return asset_defs + all_sensors
