import os
source_api_path = 'build/html/api'
arctern_prefix = '>arctern.<'
arctern_spark_prefix = '>arctern_pyspark.<'
for html_file in os.listdir(source_api_path):
    if html_file.endswith('.html'):
        with open(source_api_path + os.sep + html_file, 'r') as f:
            contents = f.read()
        contents = contents.replace('>arctern._wrapper_func.<', arctern_prefix)
        contents = contents.replace('>arctern_pyspark._wrapper_func.<', arctern_spark_prefix)
        with open(source_api_path + os.sep + html_file, 'w') as f:
            f.write(contents)
