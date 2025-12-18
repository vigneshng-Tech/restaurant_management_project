from datetime import datetime
from .models import DailyOperatingHours


def get_today_operating_hours():
    """
    Returns (open_time, close_time)for today's operating hours.
    If not found, returns (None, None)
    """
    today = datetime.now().strftime('%A')


    try:
        hours = DailyOperatingHours.objects.get(day=today)
        return hours.open_time, hours.close_time
    except DailyOperatingHours.DoesNotExist:
        return None ,None
