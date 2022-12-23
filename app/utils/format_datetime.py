from datetime import datetime


def format_datetime(record):
    record["startDate"] = datetime.strptime(
        record["startDate"], "%m/%d/%Y %I:%M %p")
    record["endDate"] = datetime.strptime(
        record["endDate"], "%m/%d/%Y %I:%M %p")

    return record
