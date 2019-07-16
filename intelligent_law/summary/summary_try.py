import numpy as np
import PyPDF2
import sys


import matplotlib.pyplot as plt

import networkx as nx


from nltk.tokenize.punkt import PunktSentenceTokenizer


from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer


# take the document as an input
def readDoc(file_name):

    # now read the type of document
    if file_name.lower().endswith('.txt'):
        choice = 1
    elif file_name.lower().endswith('.pdf'):
        choice = 2
    else:
        choice = 3

    # Case 1: if it is a .txt file

    if choice == 1:
        file_path = '/Users/warda/Desktop/INTELLIGENT LEGAL ADVISOR FYP/intelligent_law/media/' + file_name
        user_file = open(file_path, 'r', errors='ignore')
        document = user_file.read()
        user_file.close()

    # Case 2: if it is a .pdf file
    elif choice == 2:
        file_path = '/Users/warda/Desktop/INTELLIGENT LEGAL ADVISOR FYP/intelligent_law/media/' + file_name
        user_file = open(file_path, 'r', errors='ignore')
        pdfReader = PyPDF2.PdfFileReader(user_file)
        pageObj = pdfReader.getPage(0)
        document = pageObj.extractText()
        user_file.close()

    # Case 3: none of the format
    else:
        print('Failed to load a valid file')
        print('Returning an empty string')
        document = ''

   # print(type(document))
    return document


# Function to tokenize the document
# Input: String of text document
#
# Output: A list containing sentences as its elements


def tokenize(document):
    # We are tokenizing using the PunktSentenceTokenizer
    # we call an instance of this class as sentence_tokenizer
    doc_tokenizer = PunktSentenceTokenizer()

    # tokenize() method: takes our document as input and returns a list of all the sentences in the document

    # sentences is a list containing each sentence of the document as an element
    sentences_list = doc_tokenizer.tokenize(document)
    return sentences_list


def summarize_document(file_name):
    # Read the document

    # reading a file and
    # printing the size of the file
    document = readDoc(file_name)


# Generate a list of sentences in the document

    sentences_list = tokenize(document)


# Convert a collection of text documents to a matrix of token counts

    cv = CountVectorizer()
    cv_matrix = cv.fit_transform(sentences_list)
    print(cv_matrix)

    cv_demo = CountVectorizer()


# Result is 2-d matrix containing document text matrix

    normal_matrix = TfidfTransformer().fit_transform(cv_matrix)
    print(normal_matrix)
    res_graph = normal_matrix * normal_matrix.T


# Generate a graph for the document to apply PageRank algorithm

    nx_graph = nx.from_scipy_sparse_matrix(res_graph)

# Getting the rank of every sentence using pagerank

# ranks is a dictionary with key=node(sentences) and value=textrank (the rank of each of the sentences)
    ranks = nx.pagerank(nx_graph)


# Finding important sentences and generating summary

    sentence_array = sorted(
        ((ranks[i], s) for i, s in enumerate(sentences_list)), reverse=True)
    sentence_array = np.asarray(sentence_array)

    rank_max = float(sentence_array[0][0])
    rank_min = float(sentence_array[len(sentence_array) - 1][0])

    temp_array = []

    flag = 0
    if rank_max - rank_min == 0:
        temp_array.append(0)
        flag = 1

# If the sentence has different ranks
    if flag != 1:
        for i in range(0, len(sentence_array)):
            temp_array.append(
                (float(sentence_array[i][0]) - rank_min) / (rank_max - rank_min))


# Calculation of threshold:
    threshold = (sum(temp_array) / len(temp_array)) + 0.2


# Separate out the sentences that satiasfy the criteria of having a score above the threshold
    sentence_list = []
    if len(temp_array) > 1:
        for i in range(0, len(temp_array)):
            if temp_array[i] > threshold:
                sentence_list.append(sentence_array[i][1])
    else:
        sentence_list.append(sentence_array[0][1])

    model = sentence_list

#  Writing the summary to a new file

    summary = " ".join(str(x) for x in sentence_list)

# save the data in another file, names sum.txt
    f = open('/Users/warda/Desktop/INTELLIGENT LEGAL ADVISOR FYP/intelligent_law/summary/sum.txt',
             'w', encoding='utf8')

    f.write('\n')
    f.write(summary)
    f.close()

    return '\n' + summary
