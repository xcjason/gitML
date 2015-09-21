__author__ = 'jason'

from pyspark import SparkContext
import pdb

def tokenize(text):
    return text.split()

sc = SparkContext('local', 'pyspark')
text = sc.textFile('datafile.txt')
pdb.set_trace()
from operator import add
words = text.flatMap(tokenize)
pdb.set_trace()
wc = words.map(lambda x: (x, 1))
counts = wc.reduceByKey(add)
pdb.set_trace()
counts.saveAsTextFile('wc')
