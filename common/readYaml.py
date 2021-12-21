import os
from ruamel import yaml


class WRYaml:
    """ yaml文件的读和写 """

    def __init__(self):
        """ 指定yaml文件的路径 """
        self.configpath = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'datas')

    def read_yaml(self, yaml_file):
        """ 读取yaml里面里面的数据"""
        try:
            with open(os.path.join(self.configpath, yaml_file), "r", encoding='utf8') as f:
                return yaml.load(f, Loader=yaml.Loader)
        except Exception as error:
            print(f'读取yaml失败，错误如下：{error}')
            return False

    def write_yaml(self, data, yaml_file, mode='w'):
        """ 往yaml里面写入数据
            yamlFile：yaml文件名
            data：要写入的数据
            mode：写入方式： w，覆盖写入， a，追加写入
            将原数据读取出来，如果没有要加入的key，则创建一个，如果有，则执行key下面的数据修改
        """
        try:
            old_data = self.read_yaml(yaml_file) or {}
            for data_key, data_value in data.items():
                if not old_data.get(data_key):
                    old_data.setdefault(data_key, {})
                for value_key, value_value in data_value.items():
                    old_data[data_key][value_key] = value_value
            with open(os.path.join(self.configpath, yaml_file), mode, encoding="utf-8") as f:
                yaml.dump(old_data, f, Dumper=yaml.RoundTripDumper)
            return True
        except Exception as error:
            print(f'yaml文件写入失败，错误如下：\n{error}')
            return False


if __name__ == "__main__":
    wryaml = WRYaml()
    # 写入数据文件
    # data = {
    #     'test': {'AAA': 134511, 'BBB': 333}
    # }
    # # 读取数据文件