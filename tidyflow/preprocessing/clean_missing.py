# clean_missing.py
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from tidyflow.utils.logger import log_action



def clean_missing(df: pd.DataFrame, strategy: str = 'mean', threshold: float = 0.5) -> pd.DataFrame:
    """Handles missing values in a DataFrame by imputing or dropping."""
    log_action(f"Handling missing values using strategy: {strategy}")

    if strategy == 'drop':
        return df.dropna(thresh=int(threshold * len(df)), axis=1)

    imputer = SimpleImputer(strategy=strategy)
    df[df.select_dtypes(include=[np.number]).columns] = imputer.fit_transform(df.select_dtypes(include=[np.number]))
    return df
