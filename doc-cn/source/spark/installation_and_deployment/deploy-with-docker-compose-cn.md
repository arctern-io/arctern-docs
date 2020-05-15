# 基于 Docker Compose 部署

本文档介绍如何使用 Docker Compose 在单台服务器上快速部署伪分布式 Arctern-Spark 实验环境，供你体验 Arctern-Spark 接口的基本使用。

<span style="color:red">强烈建议：本文档介绍的部署方案仅供示例和体验，请勿用于生产环境中的 Arctern-Spark 部署。</span>

## 安装前提

### 系统要求

| 操作系统 | 版本 |
| ---------- | ------------ |
| CentOS     | 7 或以上      |
| Ubuntu LTS | 16.04 或以上  |

### 软件要求

| 软件名称        | 版本          | 备注  |
| ----------     | ------------ | ----- |
| Docker         | 17.06.0 或以上| 必要  |
| Docker compose | 1.17.1 或以上 | 必要  |
| Nvidia Docker  | Version 2    | 可选  |

## 配置 Docker

### 确认 Docker 运行状态

执行以下命令确认 Docker daemon 运行状态：

```bash
$ docker info
```

如果上述命令未能正常打印 Docker 相关信息，请启动 **Docker** daemon。

> **注意：** 在 Linux 环境下，Docker 命令需要 `sudo` 权限。如需要在一般权限下运行 Docker 命令，请创建 `docker` 组并添加用户。详情请参阅 [Linux 安装后步骤](https://docs.docker.com/install/linux/linux-postinstall/)。


## 配置 NVIDIA Docker （可选）

### 确认 NVIDIA Docker状态

如果需要运行 GPU 版本 Arctern-Spark，需[安装 NVIDIA Docker Version 2.0](https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0))。

执行以下命令确认 NVIDIA Docker 是否安装成功。

```bash
$ nvidia-docker version
NVIDIA Docker: 2.0.3
```

### 设置默认运行时环境

编辑 `/etc/docker/daemon.json` 文件，并添加“default-runtime“相关配置:

```json
{
    "default-runtime": "nvidia",
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    }
}
```
执行以下命令重新加载 Docker：

```bash
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker
```

## 安装并配置 Docker Compose

### 安装 Docker Compose
[安装 Docker Compose](https://docs.docker.com/compose/install/)，并执行以下命令确认 Docker Compose 的版本信息：

```bash
$ docker-compose version
```

### 下载 docker-compose.yml 文件

1. 创建 Docker Compose 工作目录
2. 下载 [docker-compose.yml](https://raw.githubusercontent.com/zilliztech/arctern-docs/branch-0.1.x/scripts/docker-compose.yml) 文件并保存至该目录。

> 如果需要运行 GPU 版本 Arctern-Spark，请将 docker-compose.yml 文件中的两处 `ARCTERN_REPO:-arcternio/arctern-spark` 修改为 `ARCTERN_REPO:-arcternio/arctern-spark-gpu`。

## 部署验证

### 启动分布式集群

在 Docker Compose 工作目录中执行以下命令启动分布式集群：

前台执行：
```bash
$ sudo docker-compose up
```

后台执行：
```bash
$ sudo docker-compose up -d
```

### 下载并执行验证代码

执行以下命令查看 Docker 容器的运行情况：

```bash
$ sudo docker ps    
# 输出如下：
CONTAINER ID        IMAGE                                                                  COMMAND                  CREATED             STATUS              PORTS                                            NAMES
acbc7dfa299f        registry.zilliz.com/arctern/arctern-spark:master-ubuntu18.04-release   "/entrypoint.sh /run…"   About an hour ago   Up About an hour                                                     docker_spark-worker_1
b7c75a456982        registry.zilliz.com/arctern/arctern-spark:master-ubuntu18.04-release   "/entrypoint.sh /run…"   About an hour ago   Up About an hour    0.0.0.0:7077->7077/tcp, 0.0.0.0:8080->8080/tcp   docker_spark-master_1
```

在 Docker 容器的运行情况中查找 NAMES 字段为“docker_spark-master_1” 的条目（在上方示例中，其 ID 为`b7c75a456982`），并执行以下命令进入 master 容器：

```bash
$ sudo docker exec -it b7c75a456982 bash
```

下载测试脚本：
```bash
$ cd /tmp
$ wget https://raw.githubusercontent.com/zilliztech/arctern/v0.1.0/spark/pyspark/examples/gis/spark_udf_ex.py
```

通过 `spark-submit` 运行脚本：
```bash
$ cd /tmp
$ spark-submit --master spark://spark-master:7077 spark_udf_ex.py
```

> **注意：** 在 `docker-compose.yml` 文件中已将 master 容器的 IP 地址映射为了 `spark-master`，因此上述命令中可用 `spark-master` 代替 master 容器的 IP 地址。另外，`docker-compose.yml` 文件中 master容器的 `7077` 端口映射到了宿主机的端口（`7077`->`7077`），因此 `spark-master` 也可以替换为宿主机的 IP 地址。


### 关闭分布式集群

在 Docker Compose 工作目录中执行以下命令关闭分布式集群：

```bash
$ sudo docker-compose down
```
