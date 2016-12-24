# -*- coding: UTF-8 -*-
# Date:'16/9/28 14:26'
__author__ = 'imaginefei'

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from optparse import OptionParser
from .yaml_tool import YamlTool
from .template_tool import TemplateTool


def render(yaml_file, template_file, objective, environment):
    # 解析yaml文件
    yaml_dict = YamlTool.load_file(yaml_file)

    # 判断解析的yaml_dict是否为复合类型
    if not isinstance(yaml_dict, dict):
        raise TypeError("yaml内容不能为纯列表")

    # 是否加入环境变量字典
    if environment:
        yaml_dict.update(os.environ.data)

    # 根据模板文件，找到模板文件夹
    template_dir = os.path.dirname(os.path.abspath(template_file))

    # 获取template_file的basename
    template_file = os.path.basename(template_file)

    # 根据模板生成文件
    tool = TemplateTool(template_dir)
    if tool.render(objective, template_file, yaml_dict):
        print "%s文件生成完毕." % objective
    else:
        print "%s文件生成失败." % objective


def main():
    # 用法描述
    usage = "%prog [options] args"
    # 解析器
    parser = OptionParser(usage)
    # 选项
    parser.add_option("-y", "--yaml", dest="yaml_file",
                      metavar="YAML_FILE", help="[必须]YAML文件（内容不能纯列表）")

    parser.add_option("-t", "--template", dest="template_file",
                      metavar="TEMPLATE_FILE", help="[必须]模板目录中的Jinja2模板文件名")

    parser.add_option("-o", "--objective", dest="objective",
                      metavar="OBJECTIVE", help="[必须]目标文件")

    parser.add_option("-e", "--environment", dest="environment",
                      action="store_true", help="加入系统环境变量到模板")

    # 参数
    (options, args) = parser.parse_args()

    # 检查必须的参数
    if options.yaml_file is None:
        parser.error("缺少yaml_file（-y）")
    elif options.template_file is None:
        parser.error("缺少template_file（-t）")
    elif options.objective is None:
        parser.error("缺少objective（-o）")

    render(options.yaml_file,
           options.template_file,
           options.objective,
           options.environment)