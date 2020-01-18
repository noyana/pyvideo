import pytest
from '../_utils' import *

def test_video_extensions():
    assert '.mp4' in video_extensions, 'mp4s not converted'
    assert '.mkv' in video_extensions, 'mkvs not converted'
    assert '.mpg' in video_extensions, 'mpgs not converted'
    assert '.avi' in video_extensions, 'avis not converted'

def test_decompose_timedelta():
    assert decompose_timedelta('') == , 'avis not converted'

def test_compose_timestring():
    assert compose_timestring(8123.45) == '02:21:23:45.':