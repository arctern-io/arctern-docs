# Arctern Restful Server 安装与配置

Arctern 提供基于 Restful 接口的 Web 服务。通过配置可将 Restful Server 与 Arctern-Spark 进行对接，从而以 Restful API 的形式提供 Arctern-Spark 的时空数据分析与展示能力。

以下将介绍 Arctern Restful Server 的安装和配置流程。更多 Arctern Restfull API 信息请查看 Restful 服务[接口文档](./api/api.html)和[使用示例](./restful_quick_start.md)。

> 注意：Arctern Restful Server 仅负责 Restful 请求的接收和解析，实际操作由 Restful Server 所连接的 Arctern-Spark 执行。在安装 Arctern Restful Server 前请确保环境存在已安装好 Arctern-Spark 的后台系统。安装 Arctern-Spark 的方式请参照其[安装文档](../spark/installation_and_deployment/installation_and_deployment.html).

## 安装准备

在安装 Arctern Restful Server 前请预先安装 MiniConda Python3。以下内容假设在 MiniConda 安装完成后进行。

### 安装依赖库

使用以下命令安装 Arctern Restful Server 的依赖库：
```bash
sudo apt install libgl-dev libosmesa6-dev libglu1-mesa-dev
```

### 创建 Conda 虚拟环境

通过以下命令为 Arctern Restful Server 构建 Conda 环境。此处假设环境名称为 `arctern_server`，用户可根据需求自行选择合适的环境名称。

```shell
conda create -n arctern_server -c conda-forge python=3.7.6
```

进入 `arctern_server` 虚拟环境：
```shell
conda activate arctern_server
```

> **注意，以下步骤需要在 conda 的 arctern 虚拟环境下进行**

### 安装 Arctern-Spark 包

Arctern Restful Server 的运行依赖于 Arctern-Spark，使用以下命令在虚拟环境中安装 Arctern-Spark 包:

```shell
conda install -y -q -c conda-forge -c arctern arctern-spark
```

> 此处安装 Arctern-Spark 仅用于解决 Restful Server 的运行时依赖，不能作为执行 Restful 请求的 Arctern-Spark 后台。

### 安装 PySpark

下载压缩包并解压：

```shell
wget https://mirror.bit.edu.cn/apache/spark/spark-3.0.0-preview2/spark-3.0.0-preview2-bin-hadoop2.7.tgz
tar zxvf spark-3.0.0-preview2-bin-hadoop2.7.tgz
```

进入解压后产生的 `spark-3.0.0-preview2-bin-hadoop2.7` 目录，执行如下命令安装 PySpark

```bash
cd python
python setup.py install
```

## 安装 Arctern Restful Server

### 基于源码的安装

从 [Arctern Github 仓库](https://github.com/zilliztech/arctern) 下载源码，在 `gui/server/arctern_server` 路径下运行以下命令构建 Arctern Restful Server 依赖环境：

```bash
pip install -r requirements.txt
```

### 基于 PIP 的安装

运行以下命令安装 Arctern Restful Server。

```bash
pip install arctern_server
```

## 配置后台 Arctern-Spark 信息

### 配置基于源码安装的 Arctern Restful Server

修改 Arctern 项目中 `gui/server/arctern_server` 路径下的 `config.ini` 文件，配置 Arctern Restful Server 所使用的 Arctern-Spark 后台信息。文件配置示例如下，其中 `spark_master_ip` 和 `port` 分别为后台 Arctern-Spark 中 master 节点的 IP 地址和端口号：

```bash
[spark]
master-addr = spark://spark_master_ip:port
```

### 配置基于 PIP 安装的 Arctern Restful Server

执行以下 Python 代码查看 Restful Server 的安装目录：

```python
import arctern_server
print(arctern_server.__path__)
```

执行上述代码将会在终端打印 Restful Server 的安装目录，修改该目录下的 `config.ini`，配置 Arctern Restful Server 所使用的 Arctern-Spark 后台信息。文件配置示例如下：

```ini
[spark]
master-addr = spark://spark_master_ip:port
```

`master-addr` 的值根据 spark 部署模式的不同有以下三种情况：

`local` 模式：

```ini
[spark]
# local[K]表示在本地启动K个worker线程，
# local表示启动一个worker线程，
# local[*]表示启动尽可能多的worker线程，数量一般等于计算机核心数，
# 具体可见 https://spark.apache.org/docs/latest/submitting-applications.html
master-addr = local[*]
```

`standalone ` 集群模式：

```ini
[spark]
# spark_master_ip 为 master 节点的 IP 地址，
# port 为 master 节点监听 spark 任务的端口号，一般为7077，
# 具体可见 https://spark.apache.org/docs/latest/spark-standalone.html
master-addr = spark://spark_master_ip:port
```

`yarn` 集群模式：

```ini
[spark]
# 具体可见 https://spark.apache.org/docs/latest/running-on-yarn.html
master-addr = yarn
```

## 启动 Arctern Restful Server

### 启动基于源码安装的 Arctern Restful Server

在 Arctern 项目的 `gui/server/arctern_server` 目录下使用以下命令启动服务，其中`/path/to/server` 为 Arctern 项目下 `gui/server` 目录的绝对路径。

```shell
# 将/path/to/arctern/gui/server替换为实际gui/server所在路径
export PYTHONPATH=/path/to/arctern/gui/server:$PYTHONPATH
python manage.py
```

### 启动基于 PIP 安装的 Arctern Restful Server

完成配置后，使用以下命令启动服务：

```shell
arctern_server
```

### 命令参数介绍

通过命令参数可在启动时对 Arctern Restful Server 进行配置，以上两种方式使用完全相同的参数，具体的内容和含义如下：


* -h：显示帮助信息

* -r：以 release 模式启动服务

* -p：为服务指定 http 端口

* -i：为服务指定 IP 地址

* --logfile= [path/to/logfile]： 配置日志文件路径信息，默认值为：` ./log.txt`

* --loglevel= [log level]：配置日志级别(debug/info/warn/error/fatal)，默认值为: `info` 

示例：

```bash
export PYTHONPATH=/path/to/server:$PYTHONPATH
python manage.py -r -i 192.168.1.2 -p 8088 
```

其中`/path/to/server` 为 Arctern 项目下 `gui/server` 目录的绝对路径。


成功完成以上步骤后，即完成了 Arctern Restful Server 的安装和配置，请参考 Arctern Restful 服务[接口文档](./api/api.html)和[使用示例](./restful_quick_start.md)使用 Arctern Restful 服务。

