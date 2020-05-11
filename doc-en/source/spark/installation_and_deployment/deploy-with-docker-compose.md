# Using docker compose to deploy Arctern

This document introduces how to deploy Arctern on a pseudo-distributed PySpark environment with Docker Compose on a singe machine. 

<span style="color:red">Notice: The introduced method deployes only a toy environment to let users try and use Arctern Spark APIs, please do NOT use it in a production environment.</span>

<!-- TOC -->

- [Prerequisites](#prerequisites)
    - [Operating system requirements](#operating-system-requirements)
    - [Software dependencies](#software-dependencies)
- [Configuring Docker](#configuring-docker)
    - [Confirm Docker status](#confirm-docker-status)
- [Configuring NVIDIA Docker (Optional)](#configuring-nvidia-docker-optional)
    - [Confirm NVIDIA Docker status](#confirm-nvidia-docker-status)
    - [Configure default runtime environment](#configure-default-runtime-environment)
- [Installing and configuring Docker compose](#installing-and-configuring-docker-compose)
    - [Install Docker compose](#install-docker-compose)
    - [Download docker-compose.yml file](#download-docker-composeyml-file)
- [Deployment Verification](#deployment-verification)
    - [Launch distributed cluster](#launch-distributed-cluster)
    - [Download and execute verification code](#download-and-execute-verification-code)
    - [Shutdown distributed cluster](#shutdown-distributed-cluster)

<!-- /TOC -->

## Prerequisites

### Operating system requirements

| Operating system   | Version  |
| ---------- | ------------ |
| CentOS     | 7 or higher      |
| Ubuntu LTS | 16.04 or higher  |

### Software dependencies

| Component        | Version          | Required?  |
| ----------     | ------------ | ----- |
| Docker         | 17.06.0 or higher| Yes  |
| Docker compose | 1.17.1 or higher | Yes  |
| Nvidia Docker  | Version 2    | No  |

## Configuring Docker

### Confirm Docker status

Use the following command to confirm the status of docker daemon:

```shell
$ docker info
```

If the command above cannot print docker information, please run **Docker** daemon.

> Note: On Linux, Docker needs sudo privileges. To run Docker command without `sudo`, create the `docker` group and add your user. For details, see the [post-installation steps for Linux](https://docs.docker.com/install/linux/linux-postinstall/).


## Configuring NVIDIA Docker (Optional)

### Confirm NVIDIA Docker status

To run Arctern with GPU support, you need to [install NVIDIA Docker Version 2.0](https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0)).

Use the following command to confirm whether NVIDIA docker is installed:

```shell
$ nvidia-docker version
NVIDIA Docker: 2.0.3
```

### Configure default runtime environment

Edit `/etc/docker/daemon.json` and add  "default-runtime" configuration:

```
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
Use the following command to reload docker:

```shell
$ sudo systemctl daemon-reload
$ sudo systemctl restart docker
```

## Installing and configuring Docker compose


### Install Docker compose
[Install Docker compose](https://docs.docker.com/compose/install/) and use the following command to confirm Docker compose version info:

```shell
$ docker-compose version
```

### Download docker-compose.yml file

Create an directory for docker compose, download [docker-compose.yml](https://raw.githubusercontent.com/zilliztech/arctern-docs/master/scripts/docker-compose.yml) file to the created directory. 

## Deployment Verification

### Launch distributed cluster

Execute the following command in the docker compose directory to launch spark cluster.

Frontend mode:
```shell
$ sudo docker-compose up
```

Backend mode:
```shell
$ sudo docker-compose up -d
```

### Download and execute verification code

Run the following command to check information of running containers:

```shell
$ sudo docker ps    # 输出如下：
CONTAINER ID        IMAGE                                                                  COMMAND                  CREATED             STATUS              PORTS                                            NAMES
acbc7dfa299f        registry.zilliz.com/arctern/arctern-spark:master-ubuntu18.04-release   "/entrypoint.sh /run…"   About an hour ago   Up About an hour                                                     docker_spark-worker_1
b7c75a456982        registry.zilliz.com/arctern/arctern-spark:master-ubuntu18.04-release   "/entrypoint.sh /run…"   About an hour ago   Up About an hour    0.0.0.0:7077->7077/tcp, 0.0.0.0:8080->8080/tcp   docker_spark-master_1
```

Enter the master container, the name of which is "docker_spark-master_1". In the example output above, the ID of master container is `b7c75a456982`.

```shell
$ sudo docker exec -it b7c75a456982 bash
```

Download verification code:

```shell
$ cd /tmp
$ wget https://raw.githubusercontent.com/zilliztech/arctern/v0.1.0/spark/pyspark/examples/gis/spark_udf_ex.py
```

Executed the verification code with `spark-submit`
```shell
$ cd /tmp
$ spark-submit --master spark://spark-master:7077 spark_udf_ex.py
```

Notice：In the `docker-compose.yml` file, the IP address of master container is mapped as `spark-master`, so we can replace the IP address of master container as `spark-master`. Besides, the `docker-compose.yml` file also mapped port `7077` of master container to `7077` port of its host server, therefore we can also replace `spark-master` with the IP address of the host server.

### Shutdown distributed cluster

Execute the following command in the docker compose directory to shutdown spark cluster.

```shell
$ sudo docker-compose down
```
