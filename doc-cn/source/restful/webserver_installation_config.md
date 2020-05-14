# Arctern RESTful Server 安装与配置

Arctern 提供基于 RESTful 接口的 Web 服务。通过配置可将 RESTful Server 与 Arctern-Spark 进行对接，从而以 RESTful API 的形式提供 Arctern-Spark 的时空数据分析与展示能力。

以下将介绍 Arctern RESTful Server 的安装和配置流程。更多 Arctern RESTful API 信息请查看 RESTful 服务[接口文档](./api/api.html)和[使用示例](./restful_quick_start.md)。

> 注意：Arctern RESTful Server 仅负责 RESTful 请求的接收和解析，实际操作由 RESTful Server 所连接的 Arctern-Spark 执行。在安装 Arctern RESTful Server 前请确保环境存在已安装好 Arctern-Spark 的后台系统。安装 Arctern-Spark 的方式请参照其[安装文档](../spark/installation_and_deployment/installation_and_deployment.html).

## 安装准备

在安装 Arctern RESTful Server 前请预先安装 Miniconda Python3，Miniconda 的安装可参考 [Linux 系统安装 Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)。以下内容假设在 Miniconda 安装完成后进行。

### 安装依赖库

执行以下命令安装 Arctern RESTful Server 的依赖库：
```bash
sudo apt install libgl-dev libosmesa6-dev libglu1-mesa-dev
```

安装 Java，建议安装 open-jdk-8：

```bash
sudo apt-get install openjdk-8-jdk
```

### 创建 Conda 虚拟环境

执行以下命令为 Arctern RESTful Server 构建 Conda 环境。此处假设环境名称为 `arctern_env`，你可根据需求自行选择合适的环境名称。

```shell
conda create -n arctern_env -c conda-forge python=3.7.6
```

进入 `arctern_env` 虚拟环境：
```shell
conda activate arctern_env
```

> 注意，以下步骤需要在 Conda 的 Arctern 虚拟环境下进行。

### 安装 Arctern-Spark 包

Arctern RESTful Server 的运行依赖于 Arctern-Spark，执行以下命令在虚拟环境中安装 Arctern-Spark 包:

```shell
conda install -y -q -c conda-forge -c arctern arctern-spark
```

> 此处安装 Arctern-Spark 仅用于解决 RESTful Server 的运行时依赖，不能作为执行 RESTful 请求的 Arctern-Spark 后台。

### 安装 PySpark

下载压缩包并解压：

```shell
wget https://mirror.bit.edu.cn/apache/spark/spark-3.0.0-preview2/spark-3.0.0-preview2-bin-hadoop2.7.tgz
tar zxvf spark-3.0.0-preview2-bin-hadoop2.7.tgz
```

进入解压后产生的 `spark-3.0.0-preview2-bin-hadoop2.7` 目录，执行如下命令安装 PySpark：

```bash
cd spark-3.0.0-preview2-bin-hadoop2.7
cd python
python setup.py install
```

## 安装 Arctern RESTful Server

### 基于源码的安装

执行以下命令安装 Arctern RESTful Server：

```bash
# 下载源码
git clone https://github.com/zilliztech/arctern.git
# 切换分支
cd arctern
git checkout master
# 安装依赖
cd gui/server/arctern_server
pip install -r requirements.txt
```

### 基于 pip 的安装

执行以下命令安装 Arctern RESTful Server：

```bash
pip install arctern_server
```

## 配置后台 Arctern-Spark 信息

Arctern RESTful Server 使用配置文件 `config.ini` 标识 Arctern-Spark 后台信息，`config.ini` 文件示例如下所示：

```ini
[spark]
master-addr = spark://spark-master:7077
```

###  查看配置文件路径

源码以及 pip 两种安装方式下 `config.ini` 配置方式稍有不同，下面分别介绍两种方式下 `config.ini` 所在路径。

#### 配置基于源码安装的 Arctern RESTful Server

使用如下命令到达 `config.ini` 文件所在目录，其中 `/path/to/arctern` 为 arctern 源代码根目录的实际路径：

```bash
cd /path/to/arctern
cd gui/server/arctern_server
```

#### 配置基于 pip 安装的 Arctern RESTful Server

执行以下 Python 代码查看 RESTful Server 的安装目录：

```python
>>> import arctern_server
>>> print(arctern_server.__path__)
['/path/to/arctern_server']
```

### 编辑配置文件

`master-addr` 的值在不同的 Spark 部署模式下有以下三种情况，请根据实际的 Spark 部署模式对配置文件进行编辑：

`local` 模式，该模式下 `config.ini` 文件内容示例如下。其中 `[]` 中的数值表示 worker 线程的数量。如果想要仅启动一个 worker 线程则可省略中括号及其中的内容。如果想要启动尽可能多的 worker 线程，请使用`local[*]` 。更加详尽的配置方式可参考 [Local 模式下 Spark 部署说明](https://spark.apache.org/docs/latest/submitting-applications.html)。

```ini
[spark]
master-addr = local[4]
```

`standalone ` 集群模式，该模式下 `config.ini` 文件内容示例如下。其中 `192.168.1.2` 为 master 节点的 IP 地址，`7077` 为 master 节点监听 spark 任务的端口号（7077 为 Spark master 节点的默认监听端口号）。请根据 Spark 集群的实际部署情况进行设置。更加详尽的配置方式可参考 [standalone 模式下 Spark 部署说明](https://spark.apache.org/docs/latest/spark-standalone.html)。

```ini
[spark]
master-addr = spark://192.168.1.2:7077
```

`yarn` 集群模式，该模式下 `config.ini` 文件内容如下。此时 spark 任务的资源管理由 Hadoop Yarn 管理，详细信息可参考 [基于 Hadoop Yarn 的 Spark 部署说明](https://spark.apache.org/docs/latest/running-on-yarn.html)。

```ini
[spark]
master-addr = yarn
```

## 启动 Arctern RESTful Server

### 启动基于源码安装的 Arctern RESTful Server

在 Arctern 项目的 `gui/server/arctern_server` 目录下执行以下命令启动服务，其中 `/path/to/arctern` 为 Arctern 项目所在目录的绝对路径。

```shell
export PYTHONPATH=/path/to/arctern/gui/server:$PYTHONPATH
python manage.py
```

### 启动基于 pip 安装的 Arctern RESTful Server

完成配置后，执行以下命令启动服务：

```shell
arctern-server
```

### 命令参数介绍

通过命令参数可在启动时对 Arctern RESTful Server 进行配置，以上两种方式使用完全相同的参数，具体的内容和含义如下：

* -h：显示帮助信息

* -r：以 release 模式启动服务

* -p：为服务指定 http 端口，默认为 `8080`

* -i：为服务指定 IP 地址，默认为本机IP `127.0.0.1`

* --logfile= [path/to/logfile]： 配置日志文件路径信息，默认值为：` ./log.txt`

* --loglevel= [log level]：配置日志级别(debug/info/warn/error/fatal)，默认值为: `info` 

示例：

```bash
export PYTHONPATH=/path/to/server:$PYTHONPATH
python manage.py -r -i 192.168.1.2 -p 8088 
```

其中 `/path/to/server` 为 Arctern 项目下 `gui/server` 目录的绝对路径。


成功完成以上步骤后，即完成了 Arctern RESTful Server 的安装和配置，请参考 Arctern RESTful 服务[接口文档](./api/api.html)和[使用示例](./restful_quick_start.md)使用 Arctern RESTful 服务。

