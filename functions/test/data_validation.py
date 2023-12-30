import unittest
import pandas as pd
import json

class TestDataValidation(unittest.TestCase):
    def test_validation_ok(self):
        
        data = {
            "client_id":"123456",
            "event_id":"456789",
            "data": [
                {
                    "date":"12-29-202300:00:00.000",
                    "value": 500,
                    "tags": ["flights", "hotels"]
                }
            ]
        }
        
        dictionary_data = json.loads(data)
        df_data = pd.DataFrame.from_dict(dictionary_data, orient="index")
        
        

        # Check the output DataFrame
        expected_output = pd.DataFrame({
            "year": [2022, 2022, 2022],
            "month": [1, 2, 3],
            "sales": [100, 200, 300]
        })

        # pd.testing.assert_frame_equal(output_data, expected_output)

# data_error = {
#     "client_id":"asdasda",
#     "event_id":"",
#     "data": [
#         {
#             "date":"12-29-202300:00:00.000",
#             "value": 500,
#             "tags": ["flights", "hotels"]
#         },
#         {
#             "date":"12-29-202301:00:00.000",
#             "value": "500",
#             "tags": None
#         },
#         {
#             "date":"12-29-202301:00:00.000",
#             "value": None,
#             "tags": ["flights"]
#         },
#         {
#             "date": None,
#             "value": "500",
#             "tags": None
#         }
#     ]
# }

# data =  {
#     "client_id":"asdasda",
#     "event_id":"",
#     "data": [
#         {
#             "date":"12-29-202300:00:00.000",
#             "value": 500,
#             "tags": ["flights", "hotels"]
#         }
#     ]
# }

# validate(data)