# Arctern RESTful Server 配置项

* `interpreter`： Arctern 数据分析后台的相关配置。
    - `interpreter_type`： 解释器类型，可选 python,pyspark。
    - `interpreter_name`： 解释器名称，如 python3。
    - `interpreter_python_path`: python 解释器所在的绝对路径。
    - `interpreter_spark_home`： Spark 所在的绝对路径。
    - `interpreter_master`： Spark master 节点模式，可选 local、standalone两种模式。
    在 local 模式下，spark 在一个物理节点内运行。配置示例如 `--interpreter_master=local[8]`，其中[8]表示使用8个 CPU。
    在 standalone 模式下，需要指定 maseter url。配置示例如`--interpreter_master=spark://IP:PORT`。
    - `interpreter_pyspark_python`： Spark executor 的 Python 解释器的绝对路径。
    - `interpreter_pyspark_driver_python`： Spark driver 的 Python 解释器的绝对路径。

* `arctern server`: Arctern RESTful Server 的相关配置。
   - `arctern_server_host`: arctern server 的 IP 地址。
   - `arctern_server_port`: arctern server 的端口号。

* `zepplin`： Arctern RESTful Server 所使用的 Zeppelin 系统的相关配置。
    - `zeppelin_port`： Zeppelin 的端口号。