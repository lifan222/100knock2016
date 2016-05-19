# -*- coding: utf-8 -*-

# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．

from knock30 import get_sentences
from collections import Counter
import matplotlib.pyplot as plt # ImportError: No module named 'matplotlib'

vocab = Counter()
for sentence in get_sentences():
    vocab += Counter(m['surface'] for m in sentence)

names, freqs = zip(*vocab.most_common())

plt.bar(range(1, len(names)+1), freqs)
plt.xscale('log')
plt.yscale('log')
plt.show()
