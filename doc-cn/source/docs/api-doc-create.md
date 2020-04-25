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

### 生成API文档

```shell
cd arctern-docs/doc-cn
mkdir build
python compile.py
```

## API文档添加

假设目前添加文件的目录结构如下：
```
package
   |---functions1.py
   |---functions2.py
   |---__init__.py
```

### 修改conf.py文件添加文件路径

```
cd doc-cn/source
vi conf.py

添加文件路径：
   sys.path.insert(2, os.path.abspath('/path/to/you/package'))
```

### 创建rst文件

这里按照上述目录结构来创建rst文件，我们这里创建三个rst文件，分别为package.rst，functions1.rst，functions2.rst,以及为为个function创建一个rst文件，假设这里functions1.py中有两个函数function1与function2，functions2.py中有两个函数function3与function4。这里我们创建如下目录。
```
package
   |----------api---
   |--package.rst  |---functions1.rst
                   |---functions2.rst
                   |---function
                          |-----function1.rst
                          |-----function2.rst
                          |-----function3.rst
                          |-----function4.rst
```

内容分别如下：
```
package.rst内容：
    Package
    =========

    .. toctree::
       :maxdepth: 2

       api/functions1
       api/functions2

functions1.rst内容如下：
    Functions1
    ===========

    .. toctree::
       :maxdepth: 2

       function/function1
       function/function2

function1.rst内容如下：
    Function1
    ==========

   .. currentmodule:: package.functions1

   .. autofunction:: function1
```

### 挂载到index.rst文件

在index.rst文件里面将package.rst文件挂载上去。内容如下：
```
.. toctree::
   :maxdepth: 2

   package/package
```

## 生成中文文档

当添加新的API或者修改英文注释时，需要修改相应的文件，添加中文注释。

### 修改compile.py文件

```python
cd doc-cn
vi compile.py

在41行添加如下代码：
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
删除41行代码：
os.system('sphinx-intl update -p build/gettext -l zh_CN')

执行：
python compile.py
```