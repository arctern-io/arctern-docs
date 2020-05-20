# 在线安装

本文档介绍在 Spark 环境中安装 Arctern 的步骤。

## 安装要求

* CPU 版本

|  名称    |   版本     |
| :---------- | :------------ |
| 操作系统 |Ubuntu LTS 18.04|
| Conda  | Miniconda Python3  |
| Spark | 3.0  |
| JDK    | JDK 8 |

* GPU 版本

|  名称    |   版本     |
| :---------- | :------------ |
| 操作系统 |Ubuntu LTS 18.04|
| Conda | Miniconda Python3  |
| Spark | 3.0  |
|CUDA|10.0|
|Nvidia driver|4.30|
| JDK    | JDK 8 |

## 安装依赖库

* CPU 版本

执行以下命令安装 Arctern-Spark CPU 版本的依赖库：
 
> **注意：** 你需要将示例中的 `</path/to/java8>` 替换为本地的 JDK 8 路径。


```bash
$ sudo apt install libgl-dev libosmesa6-dev libglu1-mesa-dev

# 配置 JDK 环境变量
$ export JAVA_HOME="</path/to/java8>"
$ export PATH=$JAVA_HOME/bin:$PATH
$ export JRE_HOME=$JAVA_HOME/jre
```

* GPU 版本

执行以下命令安装 Arctern-Spark GPU 版本的依赖库：

> **注意：** 你需要将示例中的 `</path/to/java8>` 替换为本地的 JDK 8 路径。

```bash
$ sudo apt install libgl1-mesa-dev libegl1-mesa-dev

# 配置 JDK 环境变量
$ export JAVA_HOME="</path/to/java8>"
$ export PATH=$JAVA_HOME/bin:$PATH
$ export JRE_HOME=$JAVA_HOME/jre
```

## 创建 Arctern-Spark Conda 环境

### 创建 Conda 虚拟环境

执行以下命令为 Arctern-Spark 创建 Conda 环境。此处假设环境名称为 `arctern_env`，你可根据需求自行选择合适的环境名称。

```bash
$ conda create -n arctern_env -c conda-forge python=3.7.6
```

成功创建 Conda 环境后，你可以通过 `conda env list` 命令查看所有 Conda 环境，其输出结果应包含 Arctern 环境，类似如下：
  
```bash
conda environments:
base               ...
arctern_env      ...
...
```

执行以下命令进入 arctern-env 环境：

```bash
$ conda activate arctern_env
```

> **注意：** 后续工作必须在 Arctern Conda 环境中进行。

## 安装 Arctern-Spark

* CPU 版本

执行以下命令在 Conda 环境中安装 Arctern-Spark 的 CPU 版本：

```bash
$ conda install -c arctern -c conda-forge arctern-spark
```

* GPU版本

执行以下命令在 Conda 环境中安装 Arctern-Spark 的 GPU 版本：  

```bash
$ conda install -c arctern/label/cuda10.0 -c conda-forge libarctern
$ conda install -c arctern -c conda-forge arctern-spark
```

## 安装验证

进入 Python 环境，尝试导入 `arctern` 和 `arctern_pyspark` 并确认版本是否正确。

```python
>>> import arctern
>>> import arctern_pyspark
>>> arctern.version()
>>> arctern_pyspark.version()
```

## 安装并配置 Spark

以下对 local 模式以及 standalone 单机模式下的 Spark 安装和配置流程进行介绍。若需要以集群模式安装 Spark,请参考 [Spark 官方文档](https://spark.apache.org/docs/latest/) 以及本文档末尾的 [FAQ](#FAQ)部分。

下载 [spark-3.0.0-preview2编译包](https://mirrors.sonic.net/apache/spark/spark-3.0.0-preview2/spark-3.0.0-preview2-bin-hadoop2.7.tgz) 并解压 Spark 压缩包：

```bash
$ tar -xvzf spark-3.0.0-preview2-bin-hadoop2.7.tgz
```

创建 spark-defaults.conf 以及 spark-env.sh 文件：

```bash
$ cd spark-3.0.0-preview2-bin-hadoop2.7/conf
$ cp spark-defaults.conf.template spark-defaults.conf
$ cp spark-env.sh.template spark-env.sh
```

在文件 spark-defaults.conf 的最后添加以下内容：

> **注意：** 你需要将 `<path/to/your/conda>` 替换为本地 Conda 的安装路径。执行 `conda env info` 命令可查看当前的 Conda 环境信息。

```bash
spark.executorEnv.PROJ_LIB <path/to/your/conda>/envs/arctern_env/share/proj
spark.executorEnv.GDAL_DATA <path/to/your/conda>/envs/arctern_env/share/gdal
```

在文件 spark-env.sh 的最后添加以下内容：

```bash
$ export PYSPARK_PYTHON=<path/to/your/conda>/envs/arctern_env/bin/python
```

### 确认路径配置是否成功

执行以下命令进入 PySpark 交互界面。

> **注意：** 你需要将 `<path/to/your/spark>` 替换为 Spark 的本地安装路径。

```bash
$ [path/to/your/spark]/bin/pyspark
```

在交互界面中输入以下内容打印 PySpark 的 Python 路径。

```python
>>> import sys
>>> print(sys.prefix)
```

如果终端打印了以下内容，说明 PySpark 的 Python 路径配置成功。

> **注意：** `<path/to/your/conda>` 代表 Conda 的本地安装路径。

```bash
<path/to/your/conda>/envs/arctern_env
```

## 测试样例

执行以下命令下载测试文件：

```bash
$ wget https://raw.githubusercontent.com/zilliztech/arctern/v0.1.0/spark/pyspark/examples/gis/spark_udf_ex.py
```

执行以下命令提交 Spark 任务：

> **注意：** 你需要将 `<path/to/your/spark>` 替换为 Spark 的本地安装路径，将 `<path/to/spark_udf_ex.py>` 替换为本地测试文件的路径。

local 模式：

```bash
$ <path/to/your/spark>/bin/spark-submit <path/to/spark_udf_ex.py>
```

standalone 模式：

```bash
$ <path/to/your/spark>/bin/spark-submit --master <spark service address> <path/to/spark_udf_ex.py>
```

hadoop/yarn 模式：
```bash
$ <path/to/your/spark>/bin/spark-submit --master yarn <path/to/spark_udf_ex.py>
```

若最后打印结果类似以下内容，则表示通过测试样例。
```bash
All tests of arctern have passed!
```

## 卸载

在 Conda 环境中输入以下命令可卸载 Arctern-Spark：

```bash
$ conda uninstall libarctern arctern arctern-spark
```

## FAQ

### Spark 集群模式下的安装与配置

在集群模式下（如 standalone 集群模式、hadoop/yarn 模式），你需要在每台运行 Spark 的机器上执行如下操作：

* 创建 Conda 虚拟环境
* 安装 Arctern-Spark
* 配置 Spark 环境变量

此外，在 `standalone` 集群模式下，提交任务机器的 Spark 环境需要与集群的 Spark 环境完全一致，包括以下几点：

* 集群中每台机器的 `spark` 安装路径完全一致
* 集群中每台机器的 `conda` 安装路径完全一致
* 集群中每台机器中 `conda` 虚拟环境名完全一致
