import logging
from open_data_pvnet.nwp.met_office import process_met_office_data
from open_data_pvnet.nwp.gfs import process_gfs_data
from open_data_pvnet.nwp.dwd import process_dwd_data

logger = logging.getLogger(__name__)


def handle_archive(provider, year, month, day, hour, region=None):
    """
    Handle archiving data based on the provider, year, month, day, hour, and region.

    Args:
        provider (str): The data provider (e.g., 'metoffice', 'gfs', 'dwd').
        year (int): The year of data to fetch.
        month (int): The month of data to fetch.
        day (int): The day of data to fetch.
        hour (int): The hour of data to fetch.
        region (str, optional): The region for Met Office data ('global' or 'uk'). Defaults to None.
    """
    if provider == "metoffice":
        if region not in ["global", "uk"]:
            raise ValueError(
                f"Invalid region '{region}' for provider 'metoffice'. Must be 'global' or 'uk'."
            )
        logger.info(
            f"Processing Met Office {region} data for {year}-{month:02d}-{day:02d} at hour {hour:02d}"
        )
        process_met_office_data(year, month, day, hour, region)
    elif provider == "gfs":
        logger.info(f"Fetching GFS data for {year}-{month:02d}-{day:02d} at hour {hour:02d}")
        process_gfs_data(year, month, day, hour)
    elif provider == "dwd":
        logger.info(f"Fetching DWD data for {year}-{month:02d}-{day:02d} at hour {hour:02d}")
        process_dwd_data(year, month, day, hour)
    else:
        raise ValueError(f"Unknown provider: {provider}")
