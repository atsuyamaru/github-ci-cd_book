import datetime
from zoneinfo import ZoneInfo
import os


def generate_var(date: datetime.datetime, zone: ZoneInfo) -> str:
    value = date.astimezone(zone).strftime("%Y%m%d%H%M%S")
    # Print special GitHub Actions syntax to set output
    print(f"::set-output name=timestamp::{value}")
    # For newer GitHub Actions (>= 2022), you can also use this syntax:
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f"timestamp={value}", file=fh)
    return value


if __name__ == "__main__":
    generate_var(datetime.datetime.now(), ZoneInfo("Asia/Tokyo"))
    
