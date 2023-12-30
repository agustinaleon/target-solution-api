# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app
from target_upload import *
from target_upload.utils.exceptions import TargetApiError

initialize_app()


@https_fn.on_request()
def on_request_target_upload(req: https_fn.Request) -> https_fn.Response:
    try:
       
        upload_targets(req.get_json())
        return https_fn.Response("Hello world!")
    
    except TargetApiError as e:
        print(f"An error occurred: {e}")
        
        return https_fn.Response(f"An error occurred: {str(e)}", status=e.code)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        
        return https_fn.Response(f"An error occurred: {str(e)}", status=500)
