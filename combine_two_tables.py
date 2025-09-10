import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(person, address, on="personId", how="left")
    # drop personId and addressId as per expected output
    result = merged_df.drop(columns=["personId", "addressId"])
    return result