import datetime
from target_upload.utils.constants import DATE_FORMAT
from target_upload.utils.exceptions import DateFormatError


class Format:
    def __init__(self):
        pass

    def parse(self, ):
        raise NotImplementedError("Subclass must implement abstract method")

class DateFormat(Format):
    def parse(self, date_string: str):
        try:
            datetime.datetime.strptime(date_string, DATE_FORMAT)
        except ValueError:
            raise DateFormatError(date_string)