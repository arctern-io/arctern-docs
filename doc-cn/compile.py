import os

def replace(source_api_path,src_prefix,dst_prefix):
    for html_file in os.listdir(source_api_path):
        if html_file.endswith('.html'):
           with open(source_api_path + os.sep + html_file, 'r') as f:
                contents = f.read()
           contents = contents.replace(src_prefix, dst_prefix)
           with open(source_api_path + os.sep + html_file, 'w') as f:
                f.write(contents)

if __name__ == "__main__":
    os.system('make clean')
    os.system('make html')
    os.system('make gettext')
    os.system('make html')

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