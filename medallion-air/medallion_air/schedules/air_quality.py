from dagster import (
    RunRequest,
    ScheduleEvaluationContext,
    build_schedule_from_partitioned_job,
    schedule,
)

from medallion_air.jobs.air_quality import (
    all_air_assets_job,
    all_air_assets_partitioned_job,
)

schedule_tags = {"module": __name__.split(".")[0], "type": "asset_schedule", "freq": "hourly"}

partitioned_all_assets_schedule = build_schedule_from_partitioned_job(
    job=all_air_assets_partitioned_job,
    name="hourly_partitioned_all_assets_schedule",
    description="The schedule for partitioned asset job.",
)


@schedule(
    cron_schedule="@hourly",
    job=all_air_assets_job,
    tags=schedule_tags,
    execution_timezone="Asia/Taipei",
)
def hourly_all_assets_schedule(_context: ScheduleEvaluationContext):
    scheduled_date = _context.scheduled_execution_time.strftime("%Y-%m-%d")
    run_config = {
        "ops": {
            "bronze_aqi_asset": {
                "config": {
                    "api_uri": "https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=json"
                }
            },
            "bronze_pm10_asset": {
                "config": {
                    "api_uri": "https://data.epa.gov.tw/api/v2/aqx_p_319?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=json"
                }
            },
            "bronze_pm25_asset": {
                "config": {
                    "api_uri": "https://data.epa.gov.tw/api/v2/aqx_p_02?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=json"
                }
            },
        }
    }
    return RunRequest(run_config=run_config, tags={"scheduled_date": scheduled_date})
