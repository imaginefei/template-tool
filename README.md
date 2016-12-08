# template-tool
根据jinja2模板和yaml配置文件，生成文件

## 安装
git clone https://github.com/imaginefei/template-tool.git
cd template-tool
python setup.py install

## 用法
```
$ jelly --help
Usage: jelly [options] args

Options:
  -h, --help            show this help message and exit
  -y YAML_FILE, --yaml=YAML_FILE
                        [必须]YAML文件（内容不能纯列表）
  -d TEMPLATE_DIR, --template_dir=TEMPLATE_DIR
                        [必须]模板目录
  -t TEMPLATE_FILE, --template=TEMPLATE_FILE
                        [必须]模板目录中的Jinja2模板文件名
  -o OBJECTIVE, --objective=OBJECTIVE
                        [必须]目标文件
  -e, --environment     加入系统环境变量到模板
```