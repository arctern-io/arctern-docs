import os

def replace(source_api_path,src_prefix,dst_prefix):
    for html_file in os.listdir(source_api_path):
        if html_file.endswith('.html'):
           with open(source_api_path + os.sep + html_file, 'r') as f:
                contents = f.read()
           contents = contents.replace(src_prefix, dst_prefix)
           with open(source_api_path + os.sep + html_file, 'w') as f:
                f.write(contents)

def add_content(path):
    file_read = open(path, 'r')
    udf_file_read = open('replace_udf.py','r')
    content = file_read.read()
    contentadd = udf_file_read.read()
    pos = content.find("if __name__ == '__main__':")
    file_read.close()
    udf_file_read.close()
    file_write = open(path, 'w')
    content = content[:pos] + contentadd + content[pos:]
    file_write.write(content)
    file_write.close()

def delete_content(path):
    file_read = open(path, 'r')
    content = file_read.read()
    pos_begin = content.find("import functools")
    pos_end = content.find("if __name__ == '__main__':")
    file_write = open(path, 'w')
    content = content[:pos_begin] + content[pos_end:]
    file_write.write(content)
    file_write.close()

if __name__ == "__main__":
    path = os.popen('which sphinx-build').readline().replace("\n", "")
    add_content(path)
    os.system('make clean')
    os.system('make html')
    delete_content(path)

    source_api_path = 'build/html/python/api/geospatial/function/aggr'
    src_prefix = '>arctern._wrapper_func.<'
    dst_prefix = '>arctern.<'
    replace(source_api_path,src_prefix,dst_prefix)

    source_api_path = 'build/html/python/api/geospatial/function/geospatial'
    replace(source_api_path,src_prefix,dst_prefix)

    source_api_path = 'build/html/python/api/render/function/plot'
    src_prefix = '>arctern._plot.<'
    replace(source_api_path,src_prefix,dst_prefix)

    source_api_path = 'build/html/spark/api/geospatial/function/aggr'
    src_prefix = '>arctern_pyspark._wrapper_func.<'
    dst_prefix = '>arctern_pyspark.<'
    replace(source_api_path,src_prefix,dst_prefix)

    source_api_path = 'build/html/spark/api/geospatial/function/geospatial'
    src_prefix = '>arctern_pyspark._wrapper_func.<'
    dst_prefix = '>arctern_pyspark.<' 
    replace(source_api_path,src_prefix,dst_prefix)

    source_api_path = 'build/html/spark/api/register/function'
    src_prefix = '>arctern_pyspark.register.<'
    dst_prefix = '>arctern_pyspark.<' 
    replace(source_api_path,src_prefix,dst_prefix)