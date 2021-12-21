from configparser import ConfigParser
import os

class ReadConfigFile(object):
    def read_config(self):
        conn = ConfigParser()
        file_path = os.path.join(os.path.abspath('.'),'conf.ini')
        if not os.path.exists(file_path):
            raise FileNotFoundError("文件不存在")

        conn.read(file_path)
        host = conn.get('conf','host')

        return [host]
#
# rc = ReadConfigFile()
# print(rc.read_config())