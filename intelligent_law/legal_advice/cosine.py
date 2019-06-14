import csv
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


def get_cosine_sections(absolute_path, query):
    # open penal codes excel file and load all sections into array
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

    # Create the Document Term Matrix
    count_vectorizer = CountVectorizer(stop_words='english')
    count_vectorizer = CountVectorizer()
    sparse_matrix = count_vectorizer.fit_transform(des)

    # OPTIONAL: Convert Sparse Matrix to Pandas Dataframe if you want to see the word frequencies.
    doc_term_matrix = sparse_matrix.todense()
    df = pd.DataFrame(doc_term_matrix,
                      columns=count_vectorizer.get_feature_names(),
                      )

    # Compute Cosine Similarity
    from sklearn.metrics.pairwise import cosine_similarity

    col = list(df)
    a = []

    for i in col:
        a.append(df[i][0])
    a = pd.DataFrame(a)

    a = pd.DataFrame(a)
    k = pd.DataFrame(cosine_similarity(df, a.T))
    sorted = k.sort_values(by=0, ascending=False)
    x1 = sorted[1:5]
    print(x1)

    cosine_sections = ''
    for (index, row) in x1.iterrows():
        cosine_sections = cosine_sections + 'Section # ' + str(index) + ' - ' + \
            title[index - 1][0:-1] + ', Suggestion: ' + \
            str(suggestion[index - 1]) + '<br/>'
        # print('section # ', index, ', section name: ',
        # title[index - 1], ', suggestion: ', suggestion[index - 1])

    return cosine_sections
