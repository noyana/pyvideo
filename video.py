from _utils import compose_timestring, video_extensions
import os
import ffmpeg
import json

class VideoFile(object):
    def _null_data(self):
        self.bit_rate = 0
        self.duration = "00:00:00.000"
        self.filename = '' 
        self.format_name = ''
        self.streams = 0
        self.size = 0
        self.v_codec_name = ''
        self.height = 480
        self.width = 840
        self.a_codec_name = ''
        self.a_sample_rate = 0
        self.c_date = ''
        self.m_date = ''

    def _get_data_from_file(self, filename):
        jsdata = ffmpeg.probe(filename)
        self.duration = compose_timestring(float(jsdata['format']['duration']))
        self.filename = jsdata['format']['filename'] 
        self.format_name = jsdata['format']['format_name'] 
        self.streams = jsdata['format']['nb_streams']
        self.size = int(jsdata['format']['size'])
        self.v_codec_name = jsdata['streams'][0]['codec_name'] 
        self.height = int(jsdata['streams'][0]['height'])
        self.width = int(jsdata['streams'][0]['width'])
        self.a_codec_name = jsdata['streams'][1]['codec_name'] 
        self.a_sample_rate = int(jsdata['streams'][1]['sample_rate'])
        self.c_date = os.path.getctime(filename)
        self.m_date = os.path.getmtime(filename)
        
    def __init__(self, filename):
        if os.path.isfile(filename):
            self.basename, self.extension = os.path.splitext(filename)
            if self.extension in video_extensions:
                self._get_data_from_file(filename)
            else:
                self._null_data()
        else:
            self._null_data()

    def __str__(self):
        return "".format(self.filename, self.size, )