''' 
Some service functions
'''
import datetime
video_extensions = ['.mkv', '.mp4', '.wmv', '.avi', '.mpg']
def decompose_timedelta(duration):
    ''' takes number of seconds and returns hours, minutes, seconds and miliseconds '''
    hours = duration // 3600
    minutes = (duration % 3600) // 60
    seconds = (duration % 60) // 1
    miliseconds = round((duration - hours * 3600 - minutes * 60 - seconds)*1000, 0) 
    return hours, minutes, seconds, miliseconds

def compose_timestring(duration):
    ho, min, sec, ms = decompose_timedelta(duration)
    return '{hour:02.0f}:{minute:02.0f}:{second:02.0f}.{milisecond:03.0f}'.format(hour=ho, minute=min, second=sec, milisecond=ms)

