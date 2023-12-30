import pandas as pd
from target_upload.utils.exceptions import NullValueError, LimitError, NonNumericValueError
from target_upload.validation.formats import Format


def check_null(column: pd.Series):
    if (column.isnull().values.any()):
        raise NullValueError(column.name)


def check_numeric(column: pd.Series):
    try:
        return pd.to_numeric(column)
    except Exception as e:
        raise NonNumericValueError("value error")


def check_limits(column: pd.Series, min_limit: int):
    mask = column < min_limit
    deviating_values = column[mask]
    if (deviating_values.size > 0):
        raise LimitError(-1, 0)


def check_format(column: pd.Series, format: Format):
    column.apply(format.parse)