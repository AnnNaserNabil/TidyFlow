# docs/modules.md

# API Documentation for Modules

## 1. Handling Missing Values (`clean_missing`)
```python
def clean_missing(df: pd.DataFrame, strategy: str = 'mean', threshold: float = 0.5) -> pd.DataFrame:
    """Handles missing values using specified strategy."""
```

## 2. Encoding Categorical Variables (`encode_categoricals`)
```python
def encode_categoricals(df: pd.DataFrame, method: str = 'onehot') -> pd.DataFrame:
    """Encodes categorical variables using specified encoding method."""
```

## 3. Feature Scaling (`scale_features`)
```python
def scale_features(df: pd.DataFrame, method: str = 'standard') -> pd.DataFrame:
    """Scales numerical features using the specified method."""
```

## 4. Feature Engineering (`feature_engineer`)
```python
def feature_engineer(df: pd.DataFrame, method: str = 'poly', degree: int = 2) -> pd.DataFrame:
    """Applies feature engineering techniques such as polynomial transformations."""
```

## 5. Outlier Handling (`handle_outliers`)
```python
def handle_outliers(df: pd.DataFrame, method: str = 'iqr', strategy: str = 'clip') -> pd.DataFrame:
    """Detects and handles outliers in numerical data."""
```

## 6. Automatic Data Type Inference (`auto_dtype`)
```python
def auto_dtype(df: pd.DataFrame) -> pd.DataFrame:
    """Automatically detects and converts data types."""
```

## 7. Smart Preprocessing Recommendations (`suggest_pipeline`)
```python
def suggest_pipeline(df: pd.DataFrame) -> list:
    """Provides recommendations for preprocessing steps based on dataset characteristics."""
```

## 8. Preprocessing Pipeline Builder (`build_pipeline`)
```python
def build_pipeline(df: pd.DataFrame, target_column: str = None, drop_threshold: float = 0.4) -> Pipeline:
    """Creates a Scikit-learn compatible preprocessing pipeline."""
```
