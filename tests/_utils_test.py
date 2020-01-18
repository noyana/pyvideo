import pytest
from _utils import *

def test_video_extensions():
    assert '.mp4' in video_extensions, 'mp4s not converted'
    assert '.mkv' in video_extensions, 'mkvs not converted'
    assert '.mpg' in video_extensions, 'mpgs not converted'
    assert '.avi' in video_extensions, 'avis not converted'

def test_decompose_timedelta():
    assert decompose_timedelta(8123.45) == (2, 21, 23, 45), 'time is not decompsed properly'

def test_compose_timestring():
    assert compose_timestring(8123.45) == '02:21:23:45', 'time string is not correct'