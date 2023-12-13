# Data Pre-Processing
## Theory
Data pre-processing is a critical step in the machine learning pipeline. It involves transforming raw data into a format that can be easily and effectively used for machine learning models. This process enhances the quality of data and significantly impacts the performance of models.

### `Cleaning`
Data cleaning is the first and foremost step in data pre-processing. It ensures the quality of your data by addressing issues like missing data, outliers, and duplicate records.

- **Missing Data**: Missing values can distort the statistical properties of a dataset and lead to biased estimates. Handling missing data involves techniques like imputation (filling missing values with statistical measures like mean, median, or mode) or removing records with missing values.
- **Outliers**: Outliers are data points that significantly differ from other observations. They can be a result of variability in the data or errors. Outliers can skew statistical measures and can be detrimental to the performance of some models. Techniques to manage outliers include removal, capping, or transforming these values.
- **Duplicate Data**: Duplicate entries can bias the dataset. Removing duplicates is crucial to prevent the model from overfitting.

### `Preparation`
Data preparation involves transforming and enriching the raw data into a more suitable format for modeling.

- **Feature Engineering**: This step includes adding new features or updating existing ones. It involves domain knowledge and creativity to create new variables that can significantly improve the model's performance.
- **Data Transformation**: This includes operations like aggregating data, creating interaction terms, or decomposing complex data structures. Transforming data into a format better suited for analysis is essential for effective modeling.

### `Normalization`
Normalization is a technique to standardize the range of independent variables or features of data.

- **Scaling**: Different features can be on different scales, and normalization helps to bring all the features to the same scale, ensuring that no feature dominates the model due to its scale.
- **Techniques**: Common techniques include min-max normalization, z-score normalization, and log normalization. Each technique has its pros and cons and is chosen based on the nature of the data and the model requirements.

### `Encoding`
Encoding transforms categorical data into a numerical format. Most machine learning models require numerical input.

- **Categorical Data**: These are variables that contain label values rather than numeric values. The number of possible values is often limited to a fixed set.
- **Techniques**: Common encoding techniques include one-hot encoding, label encoding, and binary encoding. The choice of encoding depends on the algorithm and the specific requirements of the dataset.

---

By expanding your theory section in this manner, you provide a more comprehensive understanding of the steps involved in data pre-processing, their importance, and how they impact the outcome of machine learning models. This approach not only educates the reader on the "how-to" but also on the "why," making it a more enriching learning experience.

---

Improving your code examples section involves enhancing clarity, providing more context, and ensuring that the examples are easily understandable and applicable. Here's an improved version of your code examples section, with added comments and additional examples for clarity:

---

## Code Examples
### Cleaning
**Handling Missing Data**
```python
# Drop rows with missing data in any column
df.dropna(inplace=True)

# Fill missing data with zero
df.fillna(0, inplace=True)

# Fill missing numerical data with the column mean
df.fillna(df.mean(), inplace=True)

# Fill missing numerical data with the column median
df.fillna(df.median(), inplace=True)

# Fill missing categorical data with the column mode (most frequent value)
df.fillna(df.mode().iloc[0], inplace=True)
```

**Handling Outliers**
```python
# Identify and remove rows with outliers in 'col'
outlier_threshold = 100
df = df[df['col'] <= outlier_threshold]

# Replace outliers in 'col' with the column mean
df.loc[df['col'] > outlier_threshold, 'col'] = df['col'].mean()
```

**Removing Duplicate Data**
```python
# Remove duplicate rows, considering all columns
df.drop_duplicates(inplace=True)
```

### Preparation
**Feature Engineering: Adding and Updating Features**
```python
# Add a new column as the sum of two other columns
df['new_col'] = df['col1'] + df['col2']

# Create a binary feature based on a condition
df['new_binary_col'] = np.where(df['col1'] > 100, 1, 0)

# Increment a numeric column by 1
df['col'] = df['col'] + 1

# Update a column based on a condition
df.loc[df['col'] > 100, 'col'] += 1
```

### Normalization
**Applying Different Normalization Techniques**
```python
# Min-Max Normalization
df['col'] = (df['col'] - df['col'].min()) / (df['col'].max() - df['col'].min())

# Z-Score Normalization
df['col'] = (df['col'] - df['col'].mean()) / df['col'].std()

# Log Normalization (ensure no zero or negative values in the column)
df['col'] = np.log(df['col'] + 1)
```

### Encoding
**One-Hot Encoding (NLP)**

#### Setting Up the Vocabulary
First, we create a vocabulary where each character is mapped to a unique integer. We'll also create an inverse mapping for decoding purposes.
```python
# Create a vocabulary
class Vocab:
    # constructor
    def __init__(self, words: Dict[str, int]):
        # words
        self.words = words
        # inverse mapping
        self.inv_words = {v: k for k, v in words.items()}
        # size of the vocabulary
        self.size = len(self.words)

vocab = Vocab(words={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5})
```

Later we create the one hot encoding, as a vector of zeros with a single 1 at the index of the character in the vocabulary.
```python
class OneHot:
    # constructor
    def __init__(self, vocab: Vocab):
        # vocab
        self.vocab = vocab

    # encode encodes a character to a one hot vector (based on the vocab)
    def encode(self, char: str) -> np.ndarray:
        # create a vector of zeros
        one_hot = np.zeros(self.vocab.size)
        # set the index of the character to 1
        one_hot[self.vocab.words[char]] = 1
        return one_hot
    
    # decode decodes a one hot vector to a character (based on the vocab)
    def decode(self, vector: np.ndarray) -> str:
        # get the index of the 1
        index = np.argmax(vector)
        # return the character at the index
        return self.vocab.inv_words[index]

# Create the encoder
one_hot = OneHot(vocab)
```

Now we can encode a word by looping through each character and one-hot encoding it.
```python
# Word to encode
word = 'face'
# Encode the word
encoded_word = np.concatenate([one_hot.encode(char) for char in word])
```