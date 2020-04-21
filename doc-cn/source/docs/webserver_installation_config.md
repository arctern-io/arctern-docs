# Arctern Restful Server 安装与配置

Arctern 提供基于 Restful 接口的 Web 服务。通过配置可将 Restful Server 与 Arctern-Spark 进行对接，从而以 Restful API 的形式提供 Arctern-Spark 的时空数据分析与展示能力。

以下将介绍 Arctern Restful Server 的安装和配置流程。更多 Arctern Restfull API 信息请查看 Restful 服务[接口文档](./restful-api.md)和[使用示例](./restful-nyc-taxi-example.md)。

## 安装准备

在安装 Arctern Restful Server 前请预先安装 MiniConda Python3。以下内容假设在 MiniConda 安装完成后进行。

### 安装 Arctern-Spark

使用以下命令安装 Arctern-Spark 的依赖库：
```bash
sudo apt install libgl-dev libosmesa6-dev libglu1-mesa-dev
```

通过以下命令为 Arctern Restful Server 构建 Conda 环境。此处假设环境名称为 `arctern_server`，用户可根据需求自行选择合适的环境名称。

```shell
conda create -n arctern_server python=3.7
```

进入 `arctern_server` 虚拟环境：
```shell
conda activate arctern_server
```

> **注意，以下步骤需要在 conda 的 arctern 虚拟环境下进行**

安装 Arctern-Spark 包:
```shell
conda install -y -q -c conda-forge -c arctern-dev arctern-spark
```

### 安装 PySpark

下载spark压缩包并解压

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

从 [Arctern Github 仓库](https://github.com/zilliztech/arctern) 下载源码，在 `gui/server` 下运行以下命令构建 Arctern Restful Server 依赖环境：

```bash
pip install -r requirements.txt
```

### 基于 PIP 的安装

运行以下命令安装 Arctern Restful Server。

```bash
pip install arctern_server
```

## 启动和配置 Arctern Restful Server

以下展示了不同使用安装方法时， Arctern Restful Server 的启动方法。 

如果基于源码安装，在 Arctern项目的 `gui/server` 目录下使用以下命令启动服务：

```shell
python manage.py
```

如果基于pip安装，使用以下命令启动服务：

```shell
arctern_server
```

通过命令参数在启动时可对 Arctern Restful Server 进行配置，以上两种方式使用完全相同的参数，具体的内容和含义如下：

```text
-h 显示帮助信息
-r 以 release 模式启动服务
-p 为服务指定 http 端口
-i 为服务指定 IP 地址
-c [path/to/data-config] 导入后台配置数据
--logfile= [path/to/logfile], default: ./log.txt' 配置日志信息
--loglevel= log level [debug/info/warn/error/fatal], default: info' 配置日志级别
```

如果希望服务器启动时自动加载数据，可以通过-c指定，例如：

```bash
python manage.py -r -c path/to/db.json
```

其中，db.json内容的格式如下：

```json
{
    "?db_name": "设定数据的名称",
    "db_name": "db1",
     "?type": "当前固定为spark",
    "type": "spark",
    "?spark": "spark配置相关",
    "spark": {
        "?app_name": "spark中运行的任务名称",
        "app_name": "arctern",
        "?master-addr": "spark地址",
        "master-addr": "local[*]",
        "?envs": "spark需要设定的环境变量",
        "envs": {
            "PYSPARK_PYTHON": "/home/ljq/miniconda3/envs/zgis_dev/bin/python"
        },
        "?configs": "spark配置相关",
        "configs": {
            "spark.sql.execution.arrow.pyspark.enabled": "true",
            "spark.databricks.session.share": "false"
        }
    },
    "?tables": "spark中需要构建的所有表",
    "tables": [
        {
            "?name": "表的名称",
            "name": "old_nyc_taxi",
            "?path": "对应的数据位置",
            "path": "/home/ljq/work/arctern/gui/server/data/0_5M_nyc_taxi_and_building.csv",
            "?format": "数据的格式",
            "format": "csv",
            "?options": "数据的相关选项设置",
            "options": {
                "header": "True",
                "delimiter": ","
            },
            "?schema": "表对应的schema",
            "schema": [
                {"VendorID": "string"},
                {"tpep_pickup_datetime": "string"},
                {"tpep_dropoff_datetime": "string"},
                {"passenger_count": "long"},
                {"trip_distance": "double"},
                {"pickup_longitude": "double"},
                {"pickup_latitude": "double"},
                {"dropoff_longitude": "double"},
                {"dropoff_latitude": "double"},
                {"fare_amount": "double"},
                {"tip_amount": "double"},
                {"total_amount": "double"},
                {"buildingid_pickup": "long"},
                {"buildingid_dropoff": "long"},
                {"buildingtext_pickup": "string"},
                {"buildingtext_dropoff": "string"}
            ],
            "?visibility": "TODO: 怎么表述，新的scope和前端api如何区分",
            "visibility": "False"
        },
        {
            "?name": "表的名称",
            "name": "nyc_taxi",
            "?sql": "生成该表的sql语句",
            "sql": "select VendorID, to_timestamp(tpep_pickup_datetime,'yyyy-MM-dd HH:mm:ss XXXXX') as tpep_pickup_datetime, to_timestamp(tpep_dropoff_datetime,'yyyy-MM-dd HH:mm:ss XXXXX') as tpep_dropoff_datetime, passenger_count, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, fare_amount, tip_amount, total_amount, buildingid_pickup, buildingid_dropoff, buildingtext_pickup, buildingtext_dropoff from old_nyc_taxi where (pickup_longitude between -180 and 180) and (pickup_latitude between -90 and 90) and (dropoff_longitude between -180 and 180) and  (dropoff_latitude between -90 and 90)",
            "visibility": "True"
        }
    ]
}
```

成功完成以上步骤后，即完成了 Arctern Restful Server 的安装和配置，请参考 Arctern Restful 服务[接口文档](./restful-api.md)和[使用示例](./restful-nyc-taxi-example.md)使用 Arctern Restful 服务。

