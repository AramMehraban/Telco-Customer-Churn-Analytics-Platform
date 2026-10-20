from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
PROCESSED_DIR = DATA_DIR / "processed"
OUTPUT_DIR = ROOT / "python" / "outputs"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize column names for consistent analysis."""
    df = df.copy()
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"[\s\-]+", "_", regex=True)
    )
    return df


def load_clean_data() -> pd.DataFrame:
    """Load the cleaned customer dataset from a known project location."""
    candidates = [
        PROCESSED_DIR / "customer_churn_clean.csv",
        PROCESSED_DIR / "telco_churn_clean.csv",
        DATA_DIR / "raw" / "Telco-Customer-Churn.csv",
        DATA_DIR / "raw" / "WA_Fn-UseC_-Telco-Customer-Churn.csv",
        DATA_DIR / "Telco-Customer-Churn.csv",
    ]

    for path in candidates:
        if path.exists():
            print(f"Loading data: {path.relative_to(ROOT)}")
            df = pd.read_csv(path)
            return normalize_columns(df)

    raise FileNotFoundError(
        "Could not locate the cleaned customer dataset.\n"
        "Expected one of these files:\n"
        + "\n".join(str(path) for path in candidates)
        + "\nCheck the data folder and update the candidates in common.py."
    )


def load_features() -> pd.DataFrame:
    """Load the feature-engineered dataset."""
    path = PROCESSED_DIR / "customer_churn_features.csv"

    if not path.exists():
        raise FileNotFoundError(
            f"Feature dataset not found: {path}\n"
            "Run 02_feature_engineering.py first."
        )

    return normalize_columns(pd.read_csv(path))


def save_output(df: pd.DataFrame, filename: str) -> Path:
    """Save a CSV output under python/outputs."""
    path = OUTPUT_DIR / filename
    df.to_csv(path, index=False)
    print(f"Saved: {path.relative_to(ROOT)}")
    return path


def require_columns(df: pd.DataFrame, columns: list[str]) -> None:
    """Raise a helpful error if required columns are missing."""
    missing = [column for column in columns if column not in df.columns]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}\n"
            f"Available columns: {list(df.columns)}"
        )


def normalize_churn(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize churn values to yes/no where possible."""
    df = df.copy()
    require_columns(df, ["churn"])

    df["churn"] = (
        df["churn"]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    return df