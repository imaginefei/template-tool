# -*- coding: UTF-8 -*-
# Date:'16/9/28 10:59'
__author__ = 'imaginefei'

from jinja2 import Environment
from jinja2 import FileSystemLoader
import logging


class TemplateTool(object):
    """
    jinja2 模板生成工具
    """
    def __init__(self, template_dir):
        """
        构造函数
        :param template_dir: 模板文件夹
        :return:
        """
        self.template_dir = template_dir

    def render(self, target_file, template_file, template_vars={}):
        """
        根据模板文件和变量，生成目标文件方法
        :param target_file: 目标文件
        :param template_file: 模板文件
        :param template_vars: 模板变量
        :return: True / False
        """
        try:
            # 判断 template_vars 类型
            if not isinstance(template_vars, dict):
                raise TypeError("template_vars 必须是字典类型")

            # 根据模板和变量生成字符串
            jinja2_env = Environment(loader=FileSystemLoader(self.template_dir))
            jinja2_template = jinja2_env.get_template(template_file)
            target_tmp = jinja2_template.render(template_vars.items())

            # 把生成的内容写入目标文件
            with open(target_file, "w+") as target:
                target.write(target_tmp.encode("utf-8"))

            return True
        except Exception, e:
            logging.exception("错误日志: %s" % e)
            return False


# if __name__ == "__main__":
#     import os
#     THIS_DIR = os.path.dirname(__file__)
#
#     tt = TemplateTool(THIS_DIR)
#
#     from yaml_tool import YamlTool
#
#     yaml_object = YamlTool.load_file("abc.yml")
#
#     print tt.render("abc.txt", "abc.j2", yaml_object)