import os
import glob
from video import VideoFile

result = []
for x in os.walk('/mnt/d/Dizi'):
    for y in glob.glob(os.path.join(x[0], '*.mkv')):
        result.append(y)
for vf in result:
    in_vid = VideoFile(vf)
    print(in_vid.filename, in_vid.v_codec_name)