import os
import glob
from video import VideoFile

result = []
for x in os.walk('/mnt/d/Dizi'):
    for y in glob.glob(os.path.join(x[0], '*.mkv')):
        result.append(y)
for vf in result:
    in_vid = VideoFile(vf)
    if in_vid.format_name != '.mp4' or \
        in_vid.height > 480 or \
        in_vid.width > 840 or \
        in_vid.bit_rate > 768:
            in_vid.convert()
    