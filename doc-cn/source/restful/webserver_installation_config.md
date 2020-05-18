# Arctern RESTful Server 安装与配置

Arctern RESTful Server 依赖于 Apache Zeppelin 以及 Conda，因此安装 Arctern RESTful Server 前需要先事先安装 Apache Zeppelin 以及 Conda。其中 Conda 建议安装 Miniconda。

## 安装 Arctern 后台

Arctern RESTful Server 仅负责 RESTful 请求的接收和解析，实际操作由 Arctern 后台执行。在安装 Arctern RESTful Server 前，你需要事先安装 Arctern 后台系统。目前 Arctern RESTful Server 支持基于 python 和基于 pyspark 的两种 Arctern 后台。

### 安装基于 Python 的 Arctern 后台

请参考如下链接：

* [安装 Arctern Python后台](../python/installation_and_deployment/install_arctern_on_python.md)

### 安装基于 pyspark 的 Arctern 后台

通过以下任意一种方式安装 Arctern 的 pyspark 后台系统：

* [在线安装](../spark/installation_and_deployment/install_arctern_on_spark_cn.md)
* [离线安装](../spark/installation_and_deployment/offline_install_arctern_on_spark_cn.md)
* [基于 Docker Compose 部署](../spark/installation_and_deployment/deploy-with-docker-compose-cn.md)

## 安装 Apache Zeppelin

使用 Arctern RESTful Server 前请先安装 Apache Zeppelin。

```bash
$ wget https://mirror.bit.edu.cn/apache/zeppelin/zeppelin-0.9.0-preview1/zeppelin-0.9.0-preview1-bin-all.tgz # 下载最新的 Zeppelin 软件包
$ tar -zxvf zeppelin-0.9.0-preview1-bin-all.tgz # 解压
```

## 安装 Miniconda

在安装 Arctern RESTful Server 前请预先安装 Miniconda。Miniconda 的安装可参考 [Linux 系统安装 Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)。

## 安装 Arctern RESTful Server

执行以下命令为 Arctern RESTful Server 构建 Conda 环境。此处假设环境名称为 `arctern_server_env`，你可根据需求自行选择合适的环境名称。

> **注意：** 如果你在同一台计算机上安装 Arctern 后台系统和 Arctern RESTful Server，请确保二者的环境名称是不同的。例如，Arctern 后台系统的名称是 `arctern_env`，Arctern RESTful Server 的名称是 `arctern_server_env`。

```bash
$ conda create -n arctern_server_env -c conda-forge python=3.7.6
```

进入 `arctern_server_env` 虚拟环境：

```bash
$ conda activate arctern_server_env
```

> **注意：** 后续工作必须在 Arctern Conda 环境中进行。

安装 Arctern RESTful Server：

```bash
$ conda install -c conda-forge arctern-webserver
```

## 服务器配置

### Zeppelin 后台配置

Zeppelin 默认在本机的 8080 端口启动后台服务，如果需要更改默认的端口号，可以修改 Zeppelin 的配置文件 `zeppelin-site.xml`：

```bash
cd zeppelin-0.9.0-preview1-bin-all
cd conf
vim zeppelin-site.xml   # 编辑配置文件
```

将下述条目中的 8080 端口替换为你想要更改的端口号：

```xml
<property>
    <name>zeppelin.server.port</name>
    <value>8080</value>
    <description>Server port.</description>
</property>
```

### Arctern RESTful Server 配置

Arctern RESTful Server 的配置文件 `config.ini` 所在目录可通过如下 Python 代码查看：

```python
>>> import arctern_server
>>> print(arctern_server.__path__)
['/path/to/arctern_server']
```

目前配置文件 `config.ini` 主要包含两个部分，分别对应字段 [zepplin] 和 [interpreter]。其中字段 [zepplin] 用于指定 Arctern RESTful Server 所使用的 Zeppelin 系统的相关信息；[interpreter] 字段用于指定 Arctern 数据分析后台的相关信息。配置文件 `config.ini` 实例如下：

```ini
[zeppelin]
zeppelin-server = localhost
zeppelin-port = 8888

[interpreter]
type = python
name = arcternpython
python-path = /path/to/python
```

[zeppelin] 字段说明如下：

- `zeppelin.zeppelin-server`： Zeppelin 后台的 IP 地址；
- `zeppelin.zeppelin-port`： Zeppelin 后台的端口号。

[interpreter] 字段说明如下：

- `interpreter.type`：解释器类型；
- `interpreter.name`：解释器名称；
- `interpreter.python-path`：装有 `Arctern` 运行环境的 python 解释器路径;

目前 Arctern RESTful Server 提供了对 `python` 和 `pyspark` 两种 Arctern 后台的适配，因此 `interpreter.type` 的可选值为 `python` 和 `pyspark` 两种，不同的后台下 `config.ini` 的配置情况稍有不同。

使用基于 python 的 Arctern 后台时，配置文件的 [interpreter] 字段示例如下：

```ini
[interpreter]
type = python
name = arcternpython
python-path = /path/to/python
```

字段说明：

- `interpreter.type`：固定为 python；
- `interpreter.name`：解释器名称；
- `interpreter.python-path`：装有 `Arctern` 运行环境的 python 解释器路径;

使用基于 pyspark 的 Arctern 后台时，配置文件的 [interpreter] 字段示例如下：

```ini
[interpreter]
type = pyspark
name = arcternpyspark
spark-home = /path/to/spark
master = local[*]
pyspark-python = python
pyspark-driver-python = python
```

字段说明：

- `interpreter.type`：固定为 pyspark；
- `interpreter.name`：解释器名称；
- `interpreter.spark-name`： spark 软件包所在路径；
- `interpreter.master`： spark master 节点配置信息；
- `interpreter.pyspark-python`： spark worker 节点运行 python 任务的解释器路径；
- `interpreter.pyspark-driver-python`： spark driver 节点提交 python 任务的解释器路径；

`interpreter.master` 的值在不同的 Spark 部署模式下有以下三种情况，请根据实际的 Spark 部署模式对配置文件进行编辑：

`local` 模式，该模式下 `config.ini` 中 `master` 字段示例如下。其中 `[]` 中的数值表示 worker 线程的数量。如果想要仅启动一个 worker 线程则可省略中括号及其中的内容。如果想要启动尽可能多的 worker 线程，请使用`local[*]` 。更加详尽的配置方式可参考 [Local 模式下 Spark 部署说明](https://spark.apache.org/docs/latest/submitting-applications.html)。

```ini
master = local[4]
```

`standalone ` 集群模式，该模式下 `config.ini` 中 `master` 字段示例如下。其中 `192.168.1.2` 为 master 节点的 IP 地址，`7077` 为 master 节点监听 spark 任务的端口号（7077 为 Spark master 节点的默认监听端口号）。请根据 Spark 集群的实际部署情况进行设置。更加详尽的配置方式可参考 [standalone 模式下 Spark 部署说明](https://spark.apache.org/docs/latest/spark-standalone.html)。

```ini
master = spark://192.168.1.2:7077
```

## 运行 Arctern RESTful Server

### 启动 Zeppelin 后台服务

启动 Arctern RESTful Server 前需要启动 Zeppelin 后台服务，使用如下命令即可启动 Zeppelin 后台服务：

```bash
$ cd zeppelin-0.9.0-preview1-bin-all
$ ./bin/zeppelin-daemon.sh start
```

### 启动 Arctern RESTful Server

完成配置后，执行以下命令启动服务：

```bash
$ arctern-server
```

### 命令参数介绍

通过命令参数可在启动时对 Arctern RESTful Server 进行配置，具体的内容和含义如下：

* -h：显示帮助信息

* -r：以 release 模式启动服务

* -p：为服务指定 http 端口，默认为 `8080`

* -i：为服务指定 IP 地址，默认为本机IP `127.0.0.1`

* --logfile= [path/to/logfile]： 配置日志文件路径信息，默认值为：` ./log.txt`

* --loglevel= [log level]：配置日志级别(debug/info/warn/error/fatal)，默认值为: `info` 

示例：

```bash
$ arctern-server -r -i 192.168.1.2 -p 8080
```

成功完成以上步骤后，即完成了 Arctern RESTful Server 的安装和配置，请参考 Arctern RESTful 服务[接口文档](./api/api.html)和[使用示例](./restful_quick_start.md)使用 Arctern RESTful 服务。
