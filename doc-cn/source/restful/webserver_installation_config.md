# Arctern RESTful Server 安装与配置

Arctern RESTful Server 依赖于 Apache Zeppelin 以及 Conda，因此安装 Arctern RESTful Server 前需要先安装 Apache Zeppelin 以及 Conda。

> **注意：** Conda 包括 Anaconda 和 Miniconda，建议使用 Miniconda。

## 安装 Arctern 后台

Arctern RESTful Server 仅负责接收和解析 RESTful 请求，实际操作由 Arctern 后台执行。在安装 Arctern RESTful Server 前，你需要事先安装 Arctern 后台系统。目前，Arctern RESTful Server 支持基于 Python 和基于 PySpark 的两种 Arctern 后台，你可以任选一种安装使用。

### 安装基于 Python 的 Arctern 后台

请参考如下链接：

* [安装 Arctern Python 后台](../python/installation_and_deployment/install_arctern_on_python.md)

### 安装基于 PySpark 的 Arctern 后台

通过以下任意一种方式安装基于 PySpark 的 Arctern 后台：

* [在线安装](../spark/installation_and_deployment/install_arctern_on_spark_cn.md)
* [离线安装](../spark/installation_and_deployment/offline_install_arctern_on_spark_cn.md)
* [基于 Docker Compose 部署](../spark/installation_and_deployment/deploy-with-docker-compose-cn.md)

## 安装 Apache Zeppelin

执行以下命令安装 Apache Zeppelin：

```bash
# 下载最新的 Zeppelin 软件包
$ wget https://mirror.bit.edu.cn/apache/zeppelin/zeppelin-0.9.0-preview1/zeppelin-0.9.0-preview1-bin-all.tgz

# 解压
$ tar -zxvf zeppelin-0.9.0-preview1-bin-all.tgz 
```

## 安装 Miniconda

Miniconda 的安装可参考 [Linux 系统安装 Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)。

## 安装 Arctern RESTful Server

1. 执行以下命令为 Arctern RESTful Server 构建 Conda 环境。此处假设环境名称为 `arctern_server_env`，你可根据需求自行选择合适的环境名称。

```bash
$ conda create -n arctern_server_env -c conda-forge python=3.7.6
```

> **注意：** 如果你在同一台计算机上安装 Arctern 后台系统和 Arctern RESTful Server，请确保二者的环境名称是不同的。例如，Arctern 后台系统的名称是 `arctern_env`，Arctern RESTful Server 的名称是 `arctern_server_env`。

2. 进入 `arctern_server_env` 虚拟环境：

```bash
$ conda activate arctern_server_env
```

> **注意：** 后续工作必须在 Arctern Conda 环境中进行。

3. 安装 Arctern RESTful Server：

```bash
$ conda install -c conda-forge arctern-webserver
```

## 配置服务器

### 配置 Zeppelin 后台

Zeppelin 默认在本机的 8080 端口启动后台服务，如果需要更改默认的端口号，执行以下命令修改 Zeppelin 的配置文件 `zeppelin-site.xml`：

```bash
cd zeppelin-0.9.0-preview1-bin-all
cd conf

# 编辑配置文件
vim zeppelin-site.xml   
```

将下方 `<value>` 标签内的 8080 替换为你想要使用的端口号：

```xml
<property>
    <name>zeppelin.server.port</name>
    <value>8080</value>
    <description>Server port.</description>
</property>
```

### 配置 Arctern RESTful Server

Arctern RESTful Server 的配置文件 `config.ini` 所在目录可通过以下 Python 代码查看：

```python
>>> import arctern_server
>>> print(arctern_server.__path__)
</path/to/arctern_server>
```

目前，Arctern RESTful Server 兼容 Python 和 PySpark 两种后台系统。因此，在不同的后台下 `config.ini` 的配置情况稍有不同。

#### 兼容 Python 的 Arctern RESTful Server 后台

兼容 Python 后台的 Arctern RESTful Server 的配置文件 `config.ini` 的示例如下：

```ini
[zeppelin]
zeppelin-server = <localhost>
zeppelin-port = 8888

[interpreter]
type = python
name = arcternpython
python-path = </path/to/python>
```

配置文件 `config.ini` 中各字段的含义如下：

* `zepplin`：指定 Arctern RESTful Server 所使用的 Zeppelin 系统的相关信息。
    - `zeppelin-server`： Zeppelin 后台的 IP 地址
    - `zeppelin-port`： Zeppelin 后台的端口号
* `interpreter`：指定 Arctern 数据分析后台的相关信息。
    - `type`：解释器类型
    - `name`：解释器名称
    - `python-path`：装有 `Arctern` 运行环境的 Python 解释器的路径

#### 兼容 PySpark 的 Arctern RESTful Server 后台

兼容 PySpark 后台的 Arctern RESTful Server 的配置文件 `config.ini` 的示例如下：

```ini
[zeppelin]
zeppelin-server = localhost
zeppelin-port = 8888

[interpreter]
type = pyspark
name = arcternpyspark
spark-home = </path/to/spark>
master = local[*]
pyspark-python = python
pyspark-driver-python = python
```

配置文件 `config.ini` 中各字段的含义如下：

* `zepplin`：指定 Arctern RESTful Server 所使用的 Zeppelin 系统的相关信息。
    - `zeppelin-server`： Zeppelin 后台的 IP 地址
    - `zeppelin-port`： Zeppelin 后台的端口号
* `interpreter`：指定 Arctern 数据分析后台的相关信息。
    - `type`：解释器类型
    - `name`：解释器名称
    - `spark-home`： Spark 软件包所在路径
    - `master`： Spark master 节点配置信息
    - `pyspark-python`： Spark worker 节点运行 Python 任务的解释器所在路径
    - `pyspark-driver-python`： Spark driver 节点提交 Python 任务的解释器所在路径

Spark 有三种不同的部署模式：`local`、`standalone`、`hadoop/yarn`。目前，Arctern RESTful Server 支持 `local` 和 `standalone` 模式，你需要根据实际使用的 Spark 部署模式编辑配置文件中 `interpreter.master` 的值：

**local 模式**

该模式下，`config.ini` 中 `interpreter.master` 字段的示例如下：

```ini
master = local[4]
```

其中，`[]` 中的数值表示 worker 线程的数量。

* 如果仅要启动一个 worker 线程，则可省略中括号及其中的内容。
* 如果要启动本机的所有 worker 线程，则使用 `local[*]` 。
* 详细的配置方式可参考 [Local 模式下 Spark 部署说明](https://spark.apache.org/docs/latest/submitting-applications.html)。

**standalone 模式**

该模式下，`config.ini` 中 `interpreter.master` 字段的示例如下：

```ini
master = spark://192.168.1.2:7077
```

其中，`192.168.1.2` 为 master 节点的 IP 地址，`7077` 为 master 节点监听 spark 任务的默认端口号。请根据你的 Spark 集群的实际部署情况进行设置。详细的配置方式可参考 [standalone 模式下 Spark 部署说明](https://spark.apache.org/docs/latest/spark-standalone.html)。

## 运行 Arctern RESTful Server

### 启动 Zeppelin 后台

启动 Arctern RESTful Server 前需要启动 Zeppelin 后台服务，执行以下命令启动 Zeppelin 后台服务：

```bash
$ cd zeppelin-0.9.0-preview1-bin-all
$ ./bin/zeppelin-daemon.sh start
```

### 启动 Arctern RESTful Server

执行以下命令启动 Arctern RESTful Server 服务：

```bash
$ arctern-server
```

#### 命令参数介绍

启动 Arctern RESTful Server 时，你可以通过命令参数对它进行配置，具体参数及其含义如下：

* -h：显示帮助信息

* -r：以 release 模式启动服务

* -p：为服务指定 http 端口，默认为 `8080`

* -i：为服务指定 IP 地址，默认为本机 IP 地址 `127.0.0.1`

* --logfile= <path/to/logfile>： 配置日志文件路径信息，默认值为：`./log.txt`

* --loglevel= <log level>：配置日志级别（debug, info, warn, error, fatal），默认值为: `info`。

使用命令参数启动 Arctern RESTful Server 的示例如下：

```bash
$ arctern-server -r -i 192.168.1.2 -p 8080
```

至此，你已经成功完成了 Arctern RESTful Server 的安装和配置。请参考 Arctern RESTful 服务[接口文档](./api/api.html)和[使用示例](./restful_quick_start.md)使用 Arctern RESTful 服务。
