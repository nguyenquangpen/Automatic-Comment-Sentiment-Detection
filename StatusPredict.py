import pandas as pd
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from lazypredict.Supervised import LazyClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report

df = pd.read_csv('D:/Academic/lap-trinh/Project/PycharmProject/Automatic_Comment_Sentiment_Detection/Data/train.csv', names=['label', 'Comment'])

#viet hoa, so, ky tu xuong dong
# print(df.isnull().sum())

def split_agglutinate(data):
    data = re.findall(r'[a-zA-Z][^A-Z]*', data)
    return ' '.join(data)

df['Comment'] = df['Comment'].apply(split_agglutinate)

# remove special characters
df['Comment'] = df['Comment'].str.translate(str.maketrans('', '', string.punctuation))

# lower case
df['Comment'] = df['Comment'].str.lower()

# remove numbers
df['Comment'] = df['Comment'].str.translate(str.maketrans('', '', string.digits))

# remove line breaks
df['Comment'] = df['Comment'].str.replace('\n', '')

# remove extra spaces
df['Comment'] = df['Comment'].str.replace(' +', ' ')

x = df['Comment']
y = df['label']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0, stratify=y)

vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=0.01, max_df=0.95)
x_train = vectorizer.fit_transform(x_train)
x_test = vectorizer.transform(x_test)

x_train = pd.DataFrame(x_train.toarray(), columns=vectorizer.get_feature_names_out())
x_test = pd.DataFrame(x_test.toarray(), columns=vectorizer.get_feature_names_out())

model = ExtraTreesClassifier(n_estimators=100, criterion='gini', random_state=42)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

def pridiction_report(text):
    if not isinstance(text, str):
        raise ValueError("Đầu vào phải là một chuỗi.")
    # remove special characters
    text = text.translate(str.maketrans('', '', string.punctuation))
    # lower case
    text = text.lower()
    # remove numbers
    text = text.translate(str.maketrans('', '', string.digits))
    # remove line breaks
    text = text.replace('\n', '')
    data_tidf = vectorizer.transform([text])
    preidc = model.predict(data_tidf)
    return preidc