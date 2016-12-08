# -*- coding: UTF-8 -*-
# Date:'16/9/28 09:34'
__author__ = 'imaginefei'

import yaml


class YamlTool(object):
    """
    yaml工具类
    """
    def __init__(self):
        pass

    @staticmethod
    def load_file(yaml_file):
        """
        解析yaml文件
        :param yaml_file: yaml文件
        :return: python对象
        """
        with open(yaml_file, "r") as f:
            yaml_object = yaml.load(f)
            return yaml_object

# if __name__ == "__main__":
#     ab = YamlTool.load_file("/tmp/yaml/a.yml")
#     print ab.get("dog")