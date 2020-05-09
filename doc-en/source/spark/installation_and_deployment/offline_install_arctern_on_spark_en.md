# Offline Installation Guide

This topic introduces how to install Arctern offline in Spark.

## TOC

<!-- TOC -->
- [Prerequisites](#prerequisites)
- [Pre-download](#predownload)
- [Setting up Arctern Conda environment](#setting-up-arctern-conda-environment)
- [Offline Installing Arctern](#offline-installing-arctern)
- [Validating installation](#validating-installation)
- [Configuring Python path for Spark](#configure-python-path-for-spark)
- [Test case](#test-case)
- [Uninstalling Arctern](#uninstalling-arctern)
- [FAQ](#faq)
    - [Support for Spark](#support-for-spark)
<!-- /TOC -->

## Prerequisites

The following environment is required for offline installation of Arctern:

 - Linux operating system
 - Conda (refer to: https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)
 - spark 3.0 (refer to: https://spark.apache.org/downloads.html)

GPU version also needs to set up the following environment:

 - CUDA Toolkit 10.0 (refer to: https://developer.nvidia.com/cuda-10.0-download-archive)
 - Nvidia driver 4.30 (refer to: https://www.nvidia.com/Download/index.aspx)

## Predownload

You need to pre-download the latest arctern conda package in a connected environment from arctern's channel.
- CPU version

    Use the following command to get and unzip package related:

    ```bash
    $ wget .......arctern_local_channel_cpu.tar.gz
    $ tar vxf arctern_local_channel_cpu.tar.gz
    $ wget ....so_dep.tar.gz
    $ tar vxf so_dep.tar.gz (add to LD_LIBRARY_PATH)
    ```

- GPU version

    Use the following command to get and unzip package related:

    ```bash
    $ wget .....arctern_local_channel_gpu.tar.gz
    $ tar vxf arctern_local_channel_gpu.tar.gz
    $ wget ....so_dep.tar.gz
    $ tar vxf so_dep.tar.gz (add to LD_LIBRARY_PATH)
    ```

## Setting up Arctern Conda Offline Environment

Use the following command to set up Arctern Conda offline environment:

```bash
$ conda config --set offline True
$ conda create -n <your_env_name>
```

After the environment is created, you can use `conda env list` to check all Conda environments. The result should include the Arctern environment.

```bash
conda environments:
base         ...
<your_env_name>      ...
...
```

Enter Arctern conda environment:

```
$ conda activate <your_env_name>
```

**Note: The following steps must be performed in the Arctern conda environment**

## Offline Installing Arctern

- CPU version

  Use the following command to install Arctern CPU version:

    ```shell
    $ conda install -c file://path_to_arctern_local_channel_cpu -n <your_env_name> arctern-spark --offline --override-channels
    ```

- GPU version

  Use the following command to install Arctern CPU version:

    ```shell
    $ conda install -c file://path_to_arctern_local_channel_gpu -n <your_env_name> arctern-spark --offline --override-channels
    ```

## Validating installation

In Python, import `arctern` and `arctern_pyspark` to validate whether the installation is successful.

```python
Python 3.7.6 | packaged by conda-forge | (default, Jan 29 2020, 14:55:04)
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import arctern
>>> import arctern_pyspark
```

## Configuring Python path for Spark

Add the following content to `conf/spark-default.conf`. `[path/to/your/conda]` is the installation path of Conda.

```bash
spark.executorEnv.PROJ_LIB [path/to/your/conda]/envs/arctern/share/proj
spark.executorEnv.GDAL_DATA [path/to/your/conda]/envs/arctern/share/gdal
```

Add the following content to `conf/spark-env.sh`. `[path/to/your/conda]` is the installation path of Conda.

```bash
export PYSPARK_PYTHON=[path/to/your/conda]/envs/arctern/bin/python
```

Check whether PySpark uses the Python path determined by `$PYSPARK_PYTHON`. `[path/to/your/spark]` is the installation path of Spark.

```python
[path/to/your/spark]/bin/pyspark
>>> import sys
>>> print(sys.prefix)
[path/to/your/conda]/envs/arctern
```

## Test case

Download test file.

```bash
wget https://raw.githubusercontent.com/zilliztech/arctern/v0.1.0/spark/pyspark/examples/gis/spark_udf_ex.py
```

Use the following command to submit Spark task. `[path/to/]spark_udf_ex.py` is the path of the test file.

```bash
# local mode
$ [path/to/your/spark]/bin/spark-submit [path/to/]spark_udf_ex.py

# standalone mode
$ [path/to/your/spark]/bin/spark-submit --master [spark service address] [path/to/]spark_udf_ex.py

# hadoop/yarn mode
$ [path/to/your/spark]/bin/spark-submit --master yarn [path/to/]spark_udf_ex.py
```

## Uninstalling Arctern

Use the following command to uninstall Arctern.

```shell
$ conda uninstall -n arctern libarctern arctern arctern-spark
```

## FAQ

### Support for Spark

Arctern can run in any mode of Spark. You must complete the following tasks for each host that runs Spark.

- Set up Conda environment
- Arctern Install Arctern
- Configure Spark environment variables

If Spark runs at `standalone` cluster mode, the Spark environment of the host that submit tasks must be consistent with the Spark environment of the cluster by:

- The absolute installation path of `spark` must be the same as each host in the cluster
- The absolute installation path of `conda` must be the same as each host in the cluster
- The name of the virtual environment must be the same as each host in the cluster
