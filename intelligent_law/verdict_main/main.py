import json
from sklearn.model_selection import cross_validate, TimeSeriesSplit, KFold
import numpy as np
import os
from my_config import ROUND_DIGITS, \
    SEED, \
    MULTILABEL_OUTPUT_FILE, \
    MULTILABEL_ARTICLES, \
    MULTILABEL_FLAVORS, \
    K_FOLD, \
    MULTILABEL_CLASSIFIERS, \
    DEFAULT_FEATURE_THRESHOLD, \
    AS_TIME_SERIES
from format import format_filter_output, format_method_output
from data import load_ECHR_instance, generate_datasets_descriptors
from scorers import make_scorers, process_score
from utils import update_classifier_result, \
    update_dataset_filter_result, \
    update_dataset_result
from collections import OrderedDict
from sklearn.tree import DecisionTreeClassifier
import json
seed = SEED
result_file = MULTILABEL_OUTPUT_FILE
articles = MULTILABEL_ARTICLES
flavors = MULTILABEL_FLAVORS
as_time_series = AS_TIME_SERIES
k_fold = K_FOLD
feature_threshold = DEFAULT_FEATURE_THRESHOLD
classifiers = MULTILABEL_CLASSIFIERS
# INPUT_PATH = 'data/input'
# INPUT_PATH1 = 'data/input1'
INPUT_PATH = '/Users/warda/Desktop/INTELLIGENT LEGAL ADVISOR FYP/intelligent_law/verdict_main/data/input'
INPUT_PATH1 = '/Users/warda/Desktop/INTELLIGENT LEGAL ADVISOR FYP/intelligent_law/verdict_main/data/input1'


dataset1 = {

    'features': os.path.join(INPUT_PATH1, 'multilabel', 'descriptive+BoW.txt'),
    'labels': os.path.join(INPUT_PATH1, 'multilabel', 'outcomes.txt'),
    'min_threshold': feature_threshold
}

X1, y1, o1 = load_ECHR_instance(
    X_file=dataset1['features'],
    y_file=dataset1['labels'],
    min_threshold=dataset1['min_threshold'],
    multilabel=True
)


clf = DecisionTreeClassifier()
clf.fit(X1, y1)

with open('/Users/warda/Desktop/INTELLIGENT LEGAL ADVISOR FYP/intelligent_law/verdict_main/cases_info_index.json') as json_file:
    data = OrderedDict(json.load(json_file))


def predict_articles(file_name):

    verdict_result = []

    # base = os.path.basename(path)
    # z = os.path.splitext(base)[0]
    z = file_name.split('.')[0]
    print(z)

    if z in data:
        f = data[z]
        n = clf.predict(X1[f])
        r = np.where(n == 1)
        y = np.concatenate(r).tolist()
        for i in y:
            if i == 1:
                verdict_result.append(
                    'Violation of Article 12 -Right to marry and start a family')
            if i == 3:
                verdict_result.append(
                    'Violation of Article 38-Obligation to furnish all necessary facilities')
            if i == 4:
                verdict_result.append('Violation of Article P4-')
            if i == 5:
                verdict_result.append(
                    'No violation of Article 13- Right to an effective remedy')
            if i == 6:
                verdict_result.append(
                    'Violation of Article 13- Right to an effective remedy')
            if i == 7:
                verdict_result.append(
                    'No violation of Article 10- Freedom of expression')
            if i == 8:
                verdict_result.append(
                    'Violation of Article 10- Freedom of expression')
            if i == 9:
                verdict_result.append(
                    'No violation of Article 1- Protection of Property')
            if i == 10:
                verdict_result.append(
                    'Violation of Article 1- Protection of Property')
            if i == 11:
                verdict_result.append(
                    'No violation of Article 9- Freedom of thought, belief and religion')
            if i == 12:
                verdict_result.append(
                    'Violation of Article 9- Freedom of thought, belief and religion')
            if i == 13:
                verdict_result.append(
                    'No violation of Article 8- Respect for your private and family life, home and correspondence')
            if i == 14:
                verdict_result.append(
                    'Violation of Article 8- Respect for your private and family life, home and correspondence')
            if i == 15:
                verdict_result.append(
                    'No violation of Article 11- Freedom of assembly and association')
            if i == 16:
                verdict_result.append(
                    'Violation of Article 11- Freedom of assembly and association')
            if i == 17:
                verdict_result.append(
                    'No violation of Article 5- Right to liberty and security')
            if i == 18:
                verdict_result.append(
                    'Violation of Article 5- Right to liberty and security')
            if i == 19:
                verdict_result.append(
                    'No violation of Article 2- Right to life')
            if i == 20:
                verdict_result.append(
                    'Violation of Article 2- Right to life')
            if i == 21:
                verdict_result.append(
                    'No violation of Article P1- Peaceful enjoyment of possessions')
            if i == 22:
                verdict_result.append(
                    'Violation of Article P1- Peaceful enjoyment of possessions')
            if i == 23:
                verdict_result.append(
                    'No violation of Article 3- Prohibition of torture')
            if i == 24:
                verdict_result.append(
                    'Violation of Article 3- Prohibition of torture')
            if i == 25:
                verdict_result.append(
                    'No violation of Article 6- Right to a fair trial')
            if i == 26:
                verdict_result.append(
                    'Violation of Article 6- Right to a fair trial')
            if i == 28:
                verdict_result.append(
                    'No violation of Article 34-  Hinder the exercise of the right of petition')
            if i == 29:
                verdict_result.append(
                    'Violation of Article 34-  Hinder the exercise of the right of petition')
            if i == 30:
                verdict_result.append(
                    'No violation of Article 7- No punishment without law')
            if i == 32:
                verdict_result.append(
                    'No violation of Article 4- Freedom from slavery and forced labour')
            if i == 33:
                verdict_result.append(
                    'Violation of Article 4- Freedom from slavery and forced labour')
    else:
        print("File not found")

    print(verdict_result)
    return verdict_result


# predict_articles('E:/verdict/raw_documents/001-171773.docx')
