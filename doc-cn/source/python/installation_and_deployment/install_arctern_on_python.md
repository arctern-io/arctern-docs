# 安装部署
本文档介绍在 python 环境中安装 Arctern 的步骤。

## 安装要求

* CPU 版本

|  名称    |   版本     |
| ---------- | ------------ |
| 操作系统 |Ubuntu LTS 18.04|
| Conda  | Miniconda Python3  |


* GPU 版本

|  名称    |   版本     |
| ---------- | ------------ |
| 操作系统 |Ubuntu LTS 18.04|
| Conda | Miniconda Python3  |
|CUDA|10.0|
|Nvidia driver|4.30|

## 安装依赖库


* CPU 版本

  使用以下命令安装 Arctern CPU 版本的依赖库：
```bash
    sudo apt install libgl-dev libosmesa6-dev libglu1-mesa-dev
```

* GPU 版本


  使用以下命令安装 Arctern GPU 版本的依赖库：
```bash
    sudo apt install libgl1-mesa-dev libegl1-mesa-dev
```

## 创建 Arctern Conda 环境

通过以下命令创建 Arctern Conda 环境。此处假设环境名称为 `arctern_python`，用户可根据需求自行选择合适的环境名称。

`conda create -n arctern_python python=3.7`

创建成功后，可以通过 `conda env list` 命令查看所有Conda环境，其输出结果应包含 Arctern 环境，类似如下：
  
  ```bash
  conda environments:
  base                ...
  arctern_python      ...
  ...
  ```

 进入 Arctern 环境：

  `conda activate arctern_python`


> **注意：后续工作必须在 Arctern Conda 环境中进行**

## 安装 Arctern


* CPU 版本
  
执行以下命令在 Conda 环境中安装 Arctern CPU 版本：

```shell
   conda install -c arctern -c conda-forge arctern
```

* GPU版本
  
执行以下命令在 Conda 环境中安装 Arctern GPU 版本：

```shell
   conda install -c arctern/label/cuda10.0 -c conda-forge libarctern 
   conda install -c arctern -c conda-forge arctern
```

## 安装验证

进入 Python 环境，尝试导入 `arctern` 验证安装是否成功。

```python
Python 3.7.6 | packaged by conda-forge | (default, Jan 29 2020, 14:55:04)
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import arctern
```

## 测试样例

安装py.test
```bash
conda install pytest
```

下载测试文件
```bash
wget https://raw.githubusercontent.com/zilliztech/arctern/v0.1.0/python/tests/geo/geo_test.py
```

通过以下命令执行测试文件
```bash
py.test [/path/to/]geo_test.py
```

若最后打印结果类似以下内容，则表示通过测试样例。
```bash
   33 passed, 1 warning in 0.58s
```

## 卸载

```shell
conda uninstall libarctern arctern
```
