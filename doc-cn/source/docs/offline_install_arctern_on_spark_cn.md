# 离线安装 
本文档介绍在 Spark 环境中离线安装 Arctern 的步骤。

## 安装要求

- CPU 版本

| 名称     | 版本              |
| -------- | ----------------- |
| 操作系统 | Ubuntu LTS 18.04  |
| Conda    | Miniconda Python3 |
| Spark    | 3.0               |

- GPU 版本

| 名称          | 版本              |
| ------------- | ----------------- |
| 操作系统      | Ubuntu LTS 18.04  |
| Conda         | Miniconda Python3 |
| Spark         | 3.0               |
| CUDA          | 10.0              |
| Nvidia driver | 418 或更高版本              |

## <span id = "installdependencies">安装依赖项</span>

### 安装系统依赖

```bash
$ git clone -b offline https://github.com/zilliztech/arctern-resources.git    # 有网环境中下载
$ cd arctern-resources/arctern_dependcies/ubuntu_dependcies
$ ./install_packages.sh gl      # 安装gl-mesa库
$ ./install_packages.sh jdk     # 安装java8
```

### 安装Spark

下载 [Spark 3.0.0-preview2](https://mirror.bit.edu.cn/apache/spark/spark-3.0.0-preview2/spark-3.0.0-preview2-bin-hadoop2.7.tgz)，并解压到指定目录


```bash
$ wget "http://mirror.bit.edu.cn/apache/spark/spark-3.0.0-preview2/spark-3.0.0-preview2-bin-hadoop2.7.tgz"       # 有网环境中下载
$ mkdir -p $SPARK_HOME && tar zxvf spark-3.0.0-preview2-bin-hadoop2.7.tgz -C $SPARK_HOME       # SPARK_HOME 为spark的安装目录
```

### 安装Miniconda

下载 [Miniconda3](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)，并执行以下命令

```bash
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh         # 有网环境中下载
$ /bin/bash ~/miniconda.sh -b -p $CONDA_HOME      # CONDA_HOME 为Conda的安装目录
```

### CUDA 环境安装（可选）

...

## 创建 Arctern Conda 离线环境

### 创建 Arctern 虚拟环境

通过以下命令创建 Arctern Conda 环境：

```bash
$ . $CONDA_HOME/etc/profile.d/conda.sh
$ conda config --set offline True
$ conda create -n arctern
```

创建成功后，可以通过 `conda env list` 命令查看所有Conda环境，其输出结果应包含Arctern环境，类似如下：

  ```bash
  conda environments:
  base         ...
  arctern      ...
  ...
  ```

 进入 Arctern 环境：

  `conda activate arctern`


**注意：后续工作必须在 Arctern 环境中进行**


## 安装 Arctern


* CPU 版本

  执行以下命令在 Conda 环境中安装 Arctern CPU 版本：

  ```bash
  $ conda install -n arctern -c file:///[path/to/channel] arctern-spark --offline   --override-channels
  ```

  例如:

  ```bash
  $ conda install -n arctern -c file:///tmp/arctern-resources/arctern_dependencies/conda_dependencies/channel arctern-spark   --offline --override-channels
  ```


* GPU版本

  执行以下命令在 Conda 环境中安装 Arctern CPU 版本：

  ```bash
      conda install -n arctern -c file:///[path/to/channel]/label/cuda10.0 libarctern   --offline --override-channels
      conda install -n arctern -c file:///[path/to/channel] arctern arctern-spark   --offline --override-channels
  ```

  例如:

  ```bash
      conda install -n arctern -c file:///tmp/arctern-resources/arctern_dependencies/conda_dependencies/channel/label/cuda10.0 libarctern --offline --override-channels
      conda install -n arctern -c file:///tmp/arctern-resources/arctern_dependencies/conda_dependencies/channel arctern   arctern-spark --offline --override-channels
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

使用测试文件检验Arctern是否安装成功,通过以下命令提交 Spark 任务。

```bash
$ cd arctern-resources/arctern_dependencies/example

# local mode
[path/to/your/spark]/bin/spark-submit spark_udf_ex.py

# standalone mode
[path/to/your/spark]/bin/spark-submit --master [spark service address] spark_udf_ex.py

# hadoop/yarn mode
[path/to/your/spark]/bin/spark-submit --master yarn spark_udf_ex.py
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
