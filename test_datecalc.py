'''
This programme runs a few unit tests against datecalc.py
'''

from datecalc import duration, when
import datetime
from datetime import timedelta

# Tests that when start date and end date are the same, the difference is 0

def test_duration():
    start_date = datetime.datetime(2021, 11, 24)
    end_date = datetime.datetime(2021, 11, 24)
    days_diff = duration(start_date, end_date)
    assert days_diff == 0
    
# Tests that the new calculated date is accurate based on how many days given
    
def test_when():
    start_date = datetime.datetime(2021, 11, 24)
    days_between = 6
    new_date = when(start_date, days_between)
    assert new_date == datetime.datetime(2021, 11, 30)
    

    