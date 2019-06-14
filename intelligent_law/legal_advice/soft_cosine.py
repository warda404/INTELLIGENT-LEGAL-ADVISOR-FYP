import csv
import pandas as pd
from gensim.matutils import softcossim
from gensim import corpora
import gensim.downloader as api
from gensim.utils import simple_preprocess
import numpy as np


def create_soft_cossim_matrix(sentences, title, des):
    len_array = np.arange(len(sentences))
    xx, yy = np.meshgrid(0, len_array)
    cossim_mat = pd.DataFrame([[round(softcossim(
        sentences[i], sentences[j], similarity_matrix), 2) for i, j in zip(x, y)] for y, x in zip(xx, yy)])
    k = cossim_mat.sort_values(by=0, ascending=False)
    k1 = pd.DataFrame(k)
    return k1


def get_soft_cosine_sections(absolute_path, query):
    file_name = absolute_path + 'intelligent_law/legal_advice/penal_codes.csv'
    f = open(file_name, errors='ignore')
    csv_file = csv.reader(f)
    des = []
    title = []
    suggestion = []
    for line in csv_file:
        suggestion.append(line[3])
        des.append(line[2])
        title.append(line[1])

    des.insert(0, query)
    fasttext_model300 = api.load('fasttext-wiki-news-subwords-300')

    # Prepare a dictionary and a corpus.
    dictionary = corpora.Dictionary(
        [simple_preprocess(doc) for doc in des])

    # Prepare the similarity matrix
    similarity_matrix = fasttext_model300.similarity_matrix(
        dictionary, tfidf=None, threshold=0.0, exponent=2.0, nonzero_limit=100)

    p = pd.Series([dictionary.doc2bow(simple_preprocess(des[i]))
                   for i in range(0, len(des))])

    valuesss = create_soft_cossim_matrix(p, title, des)
    x1 = valuesss[1:5]
    print(x1)
    soft_cosine_sections = ''
    for (index, row) in x1.iterrows():
        soft_cosine_sections = soft_cosine_sections + 'Section # ' + str(index) + ' - ' + \
            title[index - 1][0:-1] + ', Suggestion: ' + \
            str(suggestion[index - 1]) + '<br/>'
        # print('section # ', index, ', section name: ',
        #       title[index - 1], ', suggestion: ', suggestion[index - 1])

    return soft_cosine_sections
