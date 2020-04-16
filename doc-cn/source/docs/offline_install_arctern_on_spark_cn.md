# 离线安装 
本文档介绍在 Spark 环境中离线安装 Arctern 的步骤。


## 安装要求

Arctern 离线安装需要预先搭建以下环境:
 - Linux 操作系统
 - conda  ([详见官网](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html))
 - spark 3.0 （[详见官网](https://spark.apache.org/downloads.html)）
GPU 版本还需要搭建以下环境:
 - CUDA Toolkit 10.0 ([详见官网](https://developer.nvidia.com/cuda-10.0-download-archive))
 - Nvidia driver 4.30  ([详见官网](https://www.nvidia.com/Download/index.aspx))



## 预先在有网环境下载安装所需要的压缩包

* CPU 版本

  使用以下命令下载并解压相关包：
```bash
$ wget .....arctern_local_channel_cpu.tar.gz
$ tar vxf arctern_local_channel_cpu.tar.gz
$ wget ....so_dep.tar.gz
$ tar vxf so_dep.tar.gz (add to LD_LIBRARY_PATH)
```

* GPU 版本


  使用以下命令下载并解压相关包：
```bash
$ wget .....arctern_local_channel_gpu.tar.gz
$ tar vxf arctern_local_channel_gpu.tar.gz
$ wget ....so_dep.tar.gz
$ tar vxf so_dep.tar.gz (add to LD_LIBRARY_PATH)
```

## 创建 Arctern Conda 离线环境

### 创建 Arctern 虚拟环境

通过以下命令创建 Arctern Conda 环境：

```bash
$ conda config --set offline True
$ conda create -n <your_env_name>
```

创建成功后，可以通过 `conda env list` 命令查看所有Conda环境，其输出结果应包含Arctern环境，类似如下：

  ```bash
  conda environments:
  base         ...
  <your_env_name>      ...
  ...
  ```

 进入 Arctern 环境：

  `conda activate <your_env_name>`


**注意：后续工作必须在 Arctern 环境中进行**


## 安装 Arctern


* CPU 版本

  执行以下命令在 Conda 环境中安装 Arctern CPU 版本：

  ```shell
  $ conda install -c file://path_to_arctern_local_channel_cpu -n <your_env_name> arctern-spark --offline --override-channels
  ```

* GPU版本

  执行以下命令在 Conda 环境中安装 Arctern CPU 版本：

  ```shell
  $ conda install -c file://path_to_arctern_local_channel_gpu -n <your_env_name> arctern-spark --offline --override-channels
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

在 `conf/spark-default.conf` 的最后添加以下内容。其中 `[path/to/your/conda]` 为Conda的安装路径。

```bash
spark.executorEnv.PROJ_LIB [path/to/your/conda]/envs/arctern/share/proj
spark.executorEnv.GDAL_DATA [path/to/your/conda]/envs/arctern/share/gdal
```

在文件 `conf/spark-env.sh` 的最后添加以下内容。其中 `[path/to/your/conda]` 为Conda的安装路径。

```bash
export PYSPARK_PYTHON=[path/to/your/conda]/envs/arctern/bin/python
```

通过如下方式，检查 PySpark 是否使用 $PYSPARK_PYTHON 指定的 Python 路径。其中 `[path/to/your/spark]` 为 Spark 的安装路径。

```python
[path/to/your/spark]/bin/pyspark
>>> import sys
>>> print(sys.prefix)
[path/to/your/conda]/envs/arctern
```

## 测试样例

下载测试文件

```bash
wget https://raw.githubusercontent.com/zilliztech/arctern/conda/spark/pyspark/examples/gis/spark_udf_ex.py
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

## 卸载

在 Conda 环境中输入以下命令可卸载 Arctern

```shell
conda uninstall -n arctern libarctern arctern arctern-spark
```

## FAQ

### 对Spark的支持

Arctern 可以运行在 Spark 的各种模式下，需要在每台运行 Spark 的机器上，执行如下操作：

* 创建 Conda 虚拟环境
* 安装 Arctern
* 配置 Spark 环境变量

如果 Spark 运行在 `standalone` 集群模式下，提交任务机器的 Spark 环境需要与集群的 Spark 环境完全一致，包括以下几点：

* `spark` 安装的绝对路径与集群中每台机器完全一致
* `conda` 安装的绝对路径与集群中每个机器完全一致
* `conda` 虚拟环境名与集群中每个机器完全一致
