

class TargetApiError(Exception):
    pass

    
class DateFormatError(TargetApiError):
    def __init__(self, error_date):
        self.error_date = error_date
        self.code = 400
        super().__init__()

    def __str__(self):
        return  f'Wrong date format, provided: {self.error_date}, correct: MM-DD-YYYYhh:mm:ss.sss'
    

class NullValueError(TargetApiError):
    def __init__(self, error_column):
        self.error_column = error_column
        self.code = 400
        super().__init__()

    def __str__(self):
        return  f'Null value in: {self.error_column}'
    

class LimitError(TargetApiError):
    def __init__(self, error_value, min_limit):
        self.error_value = error_value
        self.min_limit = min_limit
        self.code = 400
        super().__init__()

    def __str__(self):
        return  f'Value should be greater than: {self.min_limit}, provided: {self.error_value}'
    

class NonNumericValueError(TargetApiError):
    def __init__(self, error_value):
        self.error_value = error_value
        self.code = 400
        super().__init__()

    def __str__(self):
        return  f'Non numeric value for target: {self.error_value}'
    