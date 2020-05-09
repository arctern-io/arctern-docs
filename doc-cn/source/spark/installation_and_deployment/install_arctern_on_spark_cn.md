# 在线安装
本文档介绍在 Spark 环境中安装 Arctern 的步骤。


## 安装要求

* CPU 版本

|  名称    |   版本     |
| ---------- | ------------ |
| 操作系统 |Ubuntu LTS 18.04|
| Conda  | Miniconda Python3  |
| Spark | 3.0  |


* GPU 版本

|  名称    |   版本     |
| ---------- | ------------ |
| 操作系统 |Ubuntu LTS 18.04|
| Conda | Miniconda Python3  |
| Spark | 3.0  |
|CUDA|10.0|
|Nvidia driver|4.30|



## 安装依赖库


* CPU 版本

  使用以下命令安装 Arctern-Spark CPU 版本的依赖库：
```bash
    sudo apt install libgl-dev libosmesa6-dev libglu1-mesa-dev
```

* GPU 版本


  使用以下命令安装 Arctern-Spark GPU 版本的依赖库：
```bash
    sudo apt install libgl1-mesa-dev libegl1-mesa-dev
```



## 创建 Arctern-Spark Conda 环境

### 创建 Conda 虚拟环境

通过以下命令为 Arctern-Spark 创建 Conda 环境。此处假设环境名称为 `arctern_spark`，用户可根据需求自行选择合适的环境名称。

`conda create -n arctern_spark python=3.7`

创建成功后，可以通过 `conda env list` 命令查看所有Conda环境，其输出结果应包含Arctern环境，类似如下：
  
  ```bash
  conda environments:
  base               ...
  arctern_spark      ...
  ...
  ```

 进入 Arctern-Spark 环境：

  `conda activate arctern_spark`


**注意：后续工作必须在 Arctern 环境中进行**



## 安装 Arctern-Spark


* CPU 版本

执行以下命令在 Conda 环境中安装 arctern_spark CPU 版本：

```shell
    conda install -c arctern -c conda-forge arctern-spark
```

* GPU版本

执行以下命令在 Conda 环境中安装 arctern_spark GPU 版本：  

```shell
    conda install -c arctern/label/cuda10.0 -c conda-forge libarctern
    conda install -c arctern -c conda-forge arctern-spark
```

## 安装验证

进入 Python 环境，尝试导入 `arctern` 和 `arctern_pyspark` 验证安装是否成功。

```python
Python 3.7.6 | packaged by conda-forge | (default, Jan 29 2020, 14:55:04)
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import arctern
>>> import arctern_pyspark
```

## 配置 Spark 的 Python 路径

在文件 `conf/spark-default.conf` 的最后添加以下内容。其中 `[path/to/your/conda]` 为Conda的安装路径。

```bash
spark.executorEnv.PROJ_LIB [path/to/your/conda]/envs/arctern_spark/share/proj
spark.executorEnv.GDAL_DATA [path/to/your/conda]/envs/arctern_spark/share/gdal
```

在文件 `conf/spark-env.sh` 的最后添加以下内容。其中 `[path/to/your/conda]` 为Conda的安装路径。

```bash
export PYSPARK_PYTHON=[path/to/your/conda]/envs/arctern_spark/bin/python
```

### 确认路径配置是否成功

执行以下命令进入 PySpark 交互界面，其中 `[path/to/your/spark]` 为 Spark 的安装路径。

```bash
[path/to/your/spark]/bin/pyspark
```

在交互界面中输入一下内容打印 PySpark 的 Python 路径。
```python
>>> import sys
>>> print(sys.prefix)
```

如果终端打印了一下内容，说明 PySpark 的 Python 路径配置成功。

```bash
[path/to/your/conda]/envs/arctern_spark
```

## 测试样例

下载测试文件

```bash
wget https://raw.githubusercontent.com/zilliztech/arctern/v0.1.0/spark/pyspark/examples/gis/spark_udf_ex.py
```

通过以下命令提交 Spark 任务，其中 `[path/to/]spark_udf_ex.py` 为测试文件所在的路径。

```bash
# local mode
[path/to/your/spark]/bin/spark-submit [path/to/]spark_udf_ex.py

# standalone mode
[path/to/your/spark]/bin/spark-submit --master [spark service address] [path/to/]spark_udf_ex.py

# hadoop/yarn mode
[path/to/your/spark]/bin/spark-submit --master yarn [path/to/]spark_udf_ex.py
```

若最后打印结果类似以下内容，则表示通过测试样例。
```bash
All tests of arctern have passed!
```

## 卸载

在 Conda 环境中输入以下命令可卸载 Arctern-Spark

```shell
conda uninstall libarctern arctern arctern-spark
```

## FAQ

### 对Spark的支持

Arctern-Spark 可以运行在 Spark 的各种模式下，需要在每台运行 Spark 的机器上，执行如下操作：

* 创建 Conda 虚拟环境
* 安装 Arctern-Spark
* 配置 Spark 环境变量

如果 Spark 运行在 `standalone` 集群模式下，提交任务机器的 Spark 环境需要与集群的 Spark 环境完全一致，包括以下几点：

* `spark` 安装的绝对路径与集群中每台机器完全一致
* `conda` 安装的绝对路径与集群中每个机器完全一致
* `conda` 虚拟环境名与集群中每个机器完全一致


