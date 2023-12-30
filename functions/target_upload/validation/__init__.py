import pandas as pd
from target_upload.validation.filters import *
from target_upload.utils.constants import DATE_COL, TARGET_COL
from target_upload.validation.formats import DateFormat


def validate_data(json_data: dict):
    
    df = pd.DataFrame(json_data)
    
    check_null(df[DATE_COL])
    check_null(df[TARGET_COL])
    df[TARGET_COL] = check_numeric(df[TARGET_COL])
    check_limits(df[TARGET_COL], 0)
    check_format(df[DATE_COL], DateFormat())    
    
    return df.to_json(orient='records')
    
    
def validate_metadata():
    pass  
        