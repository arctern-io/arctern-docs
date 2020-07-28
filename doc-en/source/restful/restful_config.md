# Arctern RESTful Server Configuration

* `interpreter`: Configurations for Arctern data analysis backend.
    - `interpreter_type`: Type of the interpreter. Can choose between `python` and `pyspark`.
    - `interpreter_name`: Customized name of the interpreter, such as `python3`.
    - `interpreter_python_path`: The absolute path of Python interpreter.
    - `interpreter_spark_home`: The absolute path of Spark.
    - `interpreter_master`: Spark master node mode. Can choose between `local` and `standalone` modes.

        > **Note:** 
        > * In local mode, Spark is run within a physical node. A configuration example is `--interpreter_master=local[8]`, wherein `[8]` indicates that eight CPUs are used.
        > * In standalone mode, you need to specify the master url. A configuration example is `--interpreter_master=spark://IP:PORT`.
        
    - `interpreter_pyspark_python`: The absolute path of the Python interpreter for Spark executor.
    - `interpreter_pyspark_driver_python`: The absolute path of the Python interpreter for Spark driver. 

* `arctern server`: Configurations for Arctern RESTful Server.
   - `arctern_server_host`: The IP address of Arctern RESTful Server.
   - `arctern_server_port`: The port number of Arctern RESTful Server.

* `zepplin`: Configurations for the Zeppelin system used by Arctern RESTful Server.
    - `zeppelin_port`: The port number of Zeppelin.