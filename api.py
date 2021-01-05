import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('wCHxeOSejvZjFs9uhk2E8LgxUY34WQZsIpU_PDv8TWH2')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)

visual_recognition.set_service_url('https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/7a9fb80f-49a5-4939-8cac-75fe3ddcf6cd')

with open('./3p.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file=images_file,
        classifier_ids=["default"]).get_result()
    print(json.dumps(classes, indent=2))