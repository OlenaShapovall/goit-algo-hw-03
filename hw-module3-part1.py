from datetime import datetime, timedelta


def get_days_from_today(date):
    try:
        requested_day = datetime.strptime(date, '%Y-%m-%d').date()
        today_date = datetime.today().date()
        diff_day = today_date - requested_day

        return round(diff_day.days)

    except ValueError:
        print("Incorrect entered format")


get_days_from_today("2021-01-01")


