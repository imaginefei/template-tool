# -*- coding: UTF-8 -*-
# Date:'16/9/28 09:15'
__author__ = 'imaginefei'

from setuptools import setup, find_packages


setup(
    name="jelly",
    version="1.0",
    # 把模块加入到packages列表，这里使用find_packages查找模块
    packages=find_packages("src"),
    # 告诉distutils包都在src下
    package_dir={"": "src"},
    entry_points={
        'console_scripts': ['jelly = jelly.jelly:main']
    },
    install_requires=['PyYAML>=3.12', 'jinja2>=2.8'],
    author="imaginefei",
    author_email="imaginefei@163.com",
    description="模板生成工具",
    license="GPL",
    keywords="yaml, jinja2"
)