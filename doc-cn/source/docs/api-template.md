# API注释以及Markdown文件模板

以下是一个Markdown文件模板，这里需要一个函数写一个Markdown文件。

<font size="5">**Function**</font><br /> 

**Module.Function(param1,param2,...)** [[source]](source code address)

&#x2002; &#x2003; Introduction

&#x2002; &#x2003; Parameters

&#x2002; &#x2003; &#x2002; &#x2003; * param(type) -- Introduction


&#x2002; &#x2003;Return

&#x2002; &#x2003; &#x2002; &#x2003; Introduction


&#x2002; &#x2003; Return Type
   
&#x2002; &#x2003; &#x2002; &#x2003; Introduction


&#x2002; &#x2003; Example:

  ```python
      >>> import package
      >>> xxxxxx
   ```

以下是一个函数注释模板：


  ```python
  """
    Introduction function

    :type param1: the type of param1
    :param param1: the meaning of param1 
    
    :return: intorduction of return, if success, ......

    :rtype: the type of return

    .. image:: address

    :example:
      >>> import xxx
      ......
  """
  ```