from pyhanlp import *


class Segment:

    @classmethod
    def segment(cls, corpus):
        """
        基于HanLP的分词方法
        :param corpus: 语料数据
        :return: 分词后的词列表
        """
        words = []
        nature_filter = ["g", "gb", "gbc", "gc", "gg", "gi", "gm", "gp", "h", "i", "j", "k", "l", "n", "nb", "nba",
                         "nbc", "nbp", "nf", "ng", "nh", "nhd", "nhm", "ni", "nic", "nis", "nit", "nl", "nm", "nmc",
                         "nn", "nnd", "nnt", "nr", "nr1", "nr2", "nrf", "nrj", "ns", "nsf", "nt", "ntc", "ntcb", "ntcf",
                         "ntch", "nth", "nto", "nts", "ntu", "nx", "nz", "nz", "vn"]
        for item in HanLP.segment(corpus):
            if str(item.nature) in nature_filter:
                words.append(item.word)
        return words
