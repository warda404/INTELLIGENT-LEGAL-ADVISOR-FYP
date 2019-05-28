from os import path
from collections import OrderedDict

from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier, \
							 AdaBoostClassifier, \
							 BaggingClassifier, \
							 ExtraTreesClassifier, \
							 GradientBoostingClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier

# Experiment replication
SEED = 123456
K_FOLD = 10
AS_TIME_SERIES = False

# Analysis and format
ROUND_DIGITS = 4

# General settings
ANALYSIS_PATH = 'data/analysis'
OUTPUT_PATH = 'data/output'
INPUT_PATH = 'data/input'
DEFAULT_FEATURE_THRESHOLD = 0

# ECHR specific

MULTILABEL_OUTPUT_FILE = path.join(OUTPUT_PATH, 'result_multilabel.json')
MULTILABEL_ARTICLES = ['multilabel']
MULTILABEL_FLAVORS = [ 'descriptive+BoW']
MULTILABEL_CLASSIFIERS = OrderedDict({
    
   "Decision Tree": DecisionTreeClassifier(max_depth=None),


   
}) 
