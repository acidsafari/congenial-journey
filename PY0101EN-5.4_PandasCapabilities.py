"""
Data Analysis
In this section, you will learn how to approach data acquisition in various ways,
and obtain necessary insights from a dataset. By the end of this lab,
you will successfully load the data into Jupyter Notebook,
and gain some fundamental insights via Pandas Library.

In our case, the Diabetes Dataset is an online source,
and it is in CSV (comma separated value) format.
Let's use this dataset as an example to practice data reading.

About this Dataset

Context This dataset is originally from the National Institute of Diabetes and Digestive
and Kidney Diseases. The objective of the dataset is to diagnostically predict
whether or not a patient has diabetes, based on certain diagnostic measurements
included in the dataset. Several constraints were placed on the selection of these
instances from a larger database. In particular, all patients here are females
at least 21 years old of Pima Indian heritage.

Content The datasets consists of several medical predictor variables and one target variable,
Outcome. Predictor variables includes the number of pregnancies the patient has had
 their BMI, insulin level, age, and so on.
We have 768 rows and 9 columns. The first 8 columns represent the features and
the last column represent the target/label.

"""
# Import pandas library
import pandas as pd

path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
df = pd.read_csv(path)
# show the first 5 rows using dataframe.head() method
# Contrary to dataframe.head(n), dataframe.tail(n) will show you the bottom n rows of the dataframe.
print("The first 5 rows of the dataframe")
print(df.head(5))
print(df.shape()) #for the dimensions of the DF
print(df.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 768 entries, 0 to 767
Data columns (total 9 columns):
 #   Column                    Non-Null Count  Dtype
---  ------                    --------------  -----
 0   Pregnancies               768 non-null    int64
 1   Glucose                   768 non-null    int64
 2   BloodPressure             768 non-null    int64
 3   SkinThickness             768 non-null    int64
 4   Insulin                   768 non-null    int64
 5   BMI                       768 non-null    float64
 6   DiabetesPedigreeFunction  768 non-null    float64
 7   Age                       768 non-null    int64
 8   Outcome                   768 non-null    int64
dtypes: float64(2), int64(7)
memory usage: 54.1 KB
"""
print(df.describe())

"""
Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age	Outcome
count	768.000000	768.000000	768.000000	768.000000	768.000000	768.000000	768.000000	768.000000	768.000000
mean	3.845052	120.894531	69.105469	20.536458	79.799479	31.992578	0.471876	33.240885	0.348958
std	3.369578	31.972618	19.355807	15.952218	115.244002	7.884160	0.331329	11.760232	0.476951
min	0.000000	0.000000	0.000000	0.000000	0.000000	0.000000	0.078000	21.000000	0.000000
25%	1.000000	99.000000	62.000000	0.000000	0.000000	27.300000	0.243750	24.000000	0.000000
50%	3.000000	117.000000	72.000000	23.000000	30.500000	32.000000	0.372500	29.000000	0.000000
75%	6.000000	140.250000	80.000000	32.000000	127.250000	36.600000	0.626250	41.000000	1.000000
max	17.000000	199.000000	122.000000	99.000000	846.000000	67.100000	2.420000	81.000000	1.000000
Pandas describe() is used to view some basic statistical details like percentile, mean, std etc.
of a data frame or a series of numeric values.
When this method is applied to a series of string, it returns a different output

We use Python's built-in functions to identify these missing values.
There are two methods to detect missing data:
.isnull()
.notnull()
The output is a boolean value indicating whether the value that is passed into the argument
is in fact missing data.
"True" stands for missing value, while "False" stands for not missing value.
"""
missing_data = df.isnull()
missing_data.head(5)

"""
Count missing values in each column

Using a for loop in Python, we can quickly figure out the number of missing values in each column.
As mentioned above, "True" represents a missing value, "False" means the value
is present in the dataset. In the body of the for loop the method ".value_counts()"
counts the number of "True" values.
"""
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

"""
Check all data is in the correct format (int, float, text or other).
In Pandas, we use
.dtype() to check the data type
.astype() to change the data type
Numerical variables should have type 'float' or 'int'.
"""
print(df.dtypes())

"""
Visualization is one of the best way to get insights from the dataset.
Seaborn and Matplotlib are two of Python's most powerful visualization libraries.
"""
# import libraries
import matplotlib.pyplot as plt
import seaborn as sns

labels= 'Diabetic','Not Diabetic'
plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
plt.show()
