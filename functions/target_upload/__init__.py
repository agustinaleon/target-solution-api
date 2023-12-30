from target_upload.validation import validate_data


def upload_targets(target_data: dict):
    
    date_target_data = target_data['data']
    json_data_validated = validate_data(date_target_data)
    
    #TODO
    # Validate generic data (client id, event id, year, month, etc)
    # Transform the data so its a list of objects, each object with the generic data
    # Send data to Amplitude
    