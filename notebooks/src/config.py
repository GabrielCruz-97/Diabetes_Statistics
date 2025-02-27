from pathlib import Path


PROJECT_FOLDER = Path(__file__).resolve().parents[2]

DATA_FOLDER = PROJECT_FOLDER / "data"

# path to the data files for the project
ORIGINAL_DATA = DATA_FOLDER / "diabetes.zip"
PROCESSED_DATA = DATA_FOLDER / "diabetes_processed.parquet"

# other paths deemed necessary.
IMAGES_FOLDER = PROJECT_FOLDER / "images"
