import os

def ignore_python_prompt():
    with open("build/html/_static/pygments.css", 'r') as f:
                contents = f.read()
    contents = contents.replace(".highlight .go { color: #888888 }",".highlight .go { color: #888888; -moz-user-select: none; -o-user-select:none; -khtml-user-select:none; -webkit-user-select:none; -ms-user-select:none; user-select:none }")
    contents = contents.replace(".highlight .gp { color: #000080; font-weight: bold }",".highlight .gp { color: #000080; font-weight: bold; -moz-user-select: none; -o-user-select:none; -khtml-user-select:none; -webkit-user-select:none; -ms-user-select:none; user-select:none }")
    with open("build/html/_static/pygments.css", 'w') as f:
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
    os.system('make gettext')
    os.system('make html')
    delete_content(path)
    ignore_python_prompt()