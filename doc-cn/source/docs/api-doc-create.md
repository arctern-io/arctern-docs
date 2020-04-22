# API文档添加及生成

## API文档生成

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
pip install sphinx-markdown-tables==0.0.3
pip install sphinx-intl
```

### 安装pyspark

```
cd /spark-3.0.0-preview2/python
python setup.py build && python setup.py install
```

### 修改conf.py文件

```
cd arctern-docs/doc-cn/source
vi conf.py
修改路径，如下：
    sys.path.insert(0, os.path.abspath('/path/to/python/arctern'))
	修改为当前你的文件所在的绝对路径
```

### 修改sphinx-build文件

```
使用以下指令找到sphinx-build文件路径并编辑该文件：
    which sphinx-build
    vi path/to/sphinx-build
	
在第七行添加如下代码：
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
cd arctern-docs/doc-cn
mkdir build
python compile.py
```

## API文档添加

当增加了新的对外接口函数文件需要生成API文档时，需要按照sphinx生成rst文件的流程执行一遍，生成对应的rst文件，若只是在原有的对外接口文件中新添加一个函数接口，则不需要进行这段流程，这里以新添加一个对外函数接口文件为例，具体步骤如下。

### 修改conf.py文件添加文件路径

```
cd doc-cn/source
vi conf.py

添加文件路径：
   sys.path.insert(3, os.path.abspath('/path/to/you/file'))
```

### 挂载到对应的目录下

这里假设挂载到api_py.rst下，执行如下操作：

```
cd doc-cn/source
vi api_rst.rst

将文件名称添加到api_py.rst, 添加后的代码如下：
    API
    ====

    .. toctree::
       :maxdepth: 6
       :caption: Contents:

       arctern
       new_api_file

new_api_file为新生成的rst文件名
```

### 添加函数的rst文件

下面操作是为新添加的API创建一个新的rst文件，这里需要注意的是需要为每一个新的API创建一个rst文件。

```
cd doc-cn/source/api
vi function1.rst

添加如下代码：
   function1
   =========

   .. currentmodule:: package.file_name

   .. autofunction:: function1
```

### 修改new_api_file.rst文件

```
cd doc-cn/source
vi new_api_file.rst

修改之后如下：
    ============
    NEW_API_FILE
    ============

   .. toctree::
      :maxdepth: 3
      :caption: Contents:

      /api/function1.rst
```

## 生成中文文档

当添加新的API或者修改英文注释时，需要修改相应的文件，添加中文注释。

### 修改compile.py文件

```python
cd doc-cn
vi compile.py

在23行添加如下代码：
os.system('sphinx-intl update -p build/gettext -l zh_CN')
```

### 生成并修改相应的po文件

```shell
python compile.py
cd source/locale/zh_CN/LC_MESSAGES/api

找到对应的修改或者添加的API的po文件，添加或者修改中文注释，这里我们要注几点：
       fuzzy.                                                         #如果出现该关键字，会忽略下面的注释
       msgid "Calculate the 2D Cartesian (planar) area of geometry."  #html中提取出的英文
       msgstr "计算几何体的平面面积。"                                    #这里添加英文对应的中文注释
```

### 生成中文文档

```shell
python compile.py
```