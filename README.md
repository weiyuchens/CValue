# C-value: A method for reasonable measurement of nested terms

![](https://img.shields.io/badge/language-python-blue.svg)
![](https://img.shields.io/badge/license-Apache_2.0-green.svg)

-----

一种用于合理度量嵌套术语的方法—C-value方法的实现项目。其基本思想是，首先利用词法规则生成术语候选词集合，然后使用统计信息对集合中的术语进行过滤。C-value术语自动抽取方法（Python版本）支持CLI方式对语料文本直接进行术语抽取。其中，分词技术采用工业界和学术界高度认可的`HanLP`自然语言处理工具包。

C-value提供以下功能：

* 支持多种语料输入，包括
    * CSV、TXT
* 候选术语C-value快速计算
* 候选术语集合快速排序（待完成）
* 候选术语集合多文件格式导出，包括：
    * CSV、TXT(待完成)、JSON（待完成）

### 环境配置

-----

具体的操作视操作者当前操作系统下的真实情况而定，如果系统默认的python版本就是`python3`可以直接按下面的命令操作，如果系统有多个版本可以直接见下面命令里的`python`以及`pip`改为`python3`和`pip3`。

```shell
pip install virtualenv
python -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 命令行执行

-----

INPUT_CORPUS_FILE_PATH: 需要进行术语抽取的语料的文件路径 OUTPUT_TERMS_FILE_PATH: 需要导出候选术语集合的文件路径

```shell
python main.py -i INPUT_CORPUS_FILE_PATH -o OUTPUT_TERMS_FILE_PATH
```

比如项目中的demo语料操作如下：
```shell
python main.py -i demo_corpus.csv -o result.csv
```

### API执行

-----

以demo语料操作如下：

```python
from cvalue import CValue

input_path = "demo_corpus.csv"
output_path = "result_of_csv.csv"
CValue(input_path, output_path)
```