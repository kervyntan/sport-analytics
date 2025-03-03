from datetime import datetime


def sort_by_datetime_desc(data):
    return sorted(
        data,
        key=lambda x: datetime.strptime(x["datetime"], "%Y-%m-%d %H:%M:%S"),
        reverse=True,
    )
