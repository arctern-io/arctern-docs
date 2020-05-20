# Arctern RESTful Server 安装与配置

以下为 Conda 环境下的安装过程，在安装 Arctern RESTful Server 前请安装 Conda。

> **注意：** Conda 包括 Anaconda 和 Miniconda，建议使用 Miniconda。

## 安装 Miniconda

Miniconda 的安装可参考 [Linux 系统安装 Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html)。

## 安装 Arctern 后台

Arctern RESTful Server 仅负责接收和解析 RESTful 请求，实际操作由 Arctern 后台执行。在安装 Arctern RESTful Server 前，你需要事先安装 Arctern 后台系统。目前，Arctern RESTful Server 支持基于 Python 和基于 PySpark 的两种 Arctern 后台，你可以任选一种安装使用。

### 安装基于 Python 的 Arctern 后台

请参考如下链接：

* [在线安装 Arctern Python 后台](../python/installation_and_deployment/install_arctern_on_python.md)

### 安装基于 PySpark 的 Arctern 后台

通过以下任意一种方式安装基于 PySpark 的 Arctern 后台：

* [在线安装 Arctern PySpark 后台](../spark/installation_and_deployment/install_arctern_on_spark_cn.md)
* [离线安装 Arctern PySpark 后台](../spark/installation_and_deployment/offline_install_arctern_on_spark_cn.md)

## 安装 Arctern RESTful Server

执行以下命令为 Arctern RESTful Server 构建 Conda 环境。此处使用的环境名为 `arctern_server_env`，你可根据需求自行选择合适的环境名称。

```bash
$ conda create -n arctern_server_env -c conda-forge python=3.7.6
```

> **注意：** 如果你在同一台计算机上安装 Arctern 后台系统和 Arctern RESTful Server，建议二者使用不同的 Conda 环境。例如，为 Arctern 后台创建名为 `arctern_env` 的环境，为 Arctern RESTful Server 的创建名为 `arctern_server_env` 的环境。

进入 `arctern_server_env` 虚拟环境：

```bash
$ conda activate arctern_server_env
```

安装 Arctern RESTful Server：

```bash
$ conda install -c conda-forge -c arctern arctern-webserver
```

## 设置 Arctern RESTful Server Workspace

workspace 用于存放 Arctern RESTful Server 所依赖的第三方工具、插件、系统配置文件等信息。在初次启动 RESTful Server 前，你需要通过 Bootstrap 命令设置 workspace。

```bash
arctern-server bootstrap --workspace=/home/usr/arctern_server/
```

## 配置 Arctern RESTful Server

Arctern RESTful Server 为用户开放了一组系统配置项，包括服务端口、IP地址、数据处理后台等。其中，Python 或 PySpark 等不同的数据处理后台的选择由 interpreter_type 选项控制。

如果选用 Python 作为后台，请依照以下命令示例进行配置，配置项解释详见 [Arctern RESTful Server 配置选项](./restful_config.md)：

```bash
arctern-server config --arctern_server_host=127.0.0.1 --arctern_server_port=8080 --interpreter_type=python --interpreter_name=arcternpython --interpreter_python_path="</path/to/python>"
```

如果选用 PySpark 作为后台，请依照以下命令示例进行配置，配置项解释详见 [Arctern RESTful Server 配置选项](./restful_config.md)：

```bash
arctern-server config --arctern_server_host=127.0.0.1 --arctern_server_port=8080 --interpreter_type=pyspark --interpreter_name=arcternpyspark --interpreter_pyspark_python="</path/to/python>" --interpreter_pyspark_driver_python=</path/to/python> --interpreter_spark_home="</path/to/spark>" --interpreter_master=local[*]
```

> **注意：** 你需要将 `</path/to/file>` 替换为 Arctern 所在的 Conda 环境内对应文件的绝对路径。

## 启动

```bash
arctern-server start --mode=release
```

`mode` 可选 `release` 或 `debug`。debug 模式会提供更准确的提示信息，但比 release 模式的执行效率低。

## FAQ

使用 http 代理对运行 Arctern RESTful Server 的影响：

使用 http 代理可能会导致 RESTful API 无法被正常调用，请关闭 http 代理然后重启 Arctern RESTful Server。
