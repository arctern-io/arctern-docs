# API文档添加及生成

## 大纲
* [API文档生成](#create)

## <span id = "create">API文档生成</span>

### 环境准备

操作系统  | 版本
:-----------:|:----------:
Ubuntu LTS  | 18.04 或以上

|软件名称  |
|:-----------:|
|miniconda（推荐） 或者 anaconda  |

### 安装所需包

```
conda install sphinx
pip install sphinx_automodapi
pip install sphinx_rtd_theme
pip install --upgrade recommonmark
```

### 安装pyspark

```
cd /spark-3.0.0-preview2/python
python setup.py build && python setup.py install
```

### 修改conf.py文件

```
cd arctern-docs/api-doc/source
vim conf.py
修改路径，如下：
    sys.path.insert(0, os.path.abspath('/path/to/python/arctern'))
	修改为当前你的文件所在的绝对路径
```
使用以下指令找到sphinx-build文件路径：
    which sphinx-build
	
添加如下代码：
    import functools
    from pyspark.sql import functions

### 修改sphinx-build文件

```
使用以下指令找到sphinx-build文件路径：
    which sphinx-build
	
添加如下代码：
    import functools
    from pyspark.sql import functions

    def pandas_udf(p1, p2):

       from functools import wraps
       def inner(func):
           @wraps(func)
           def wrapper(*args, **kwargs):
               result = func(*args, **kwargs)
               return result
           return wrapper

       return inner

    functions.pandas_udf=pandas_udf
```

### 生成API文档

```shell
cd arctern/doc/api-doc
mkdir build
make clean
make html
python replace.py
```