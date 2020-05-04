import boto3
from pprint import pprint
from image_helper import get_image_from_file, get_image_from_url

def detect_labels_data(image_bytes):
    client = boto3.client('rekognition')
    response = client.detect_labels(Image={'Bytes': image_bytes}, MinConfidence=50)
    pprint(f'{response}')

def detect_labels(image_bytes):
    client = boto3.client('rekognition')
    response = client.detect_labels(Image={'Bytes': image_bytes}, MinConfidence=50)
    print('\n\nLabels:')
    for label in response['Labels']:
        label_name = label['Name']
        label_confidence = label['Confidence']
        print(f' {label_name}  --  {round(label_confidence, 2)}%')


url = 'https://arc-anglerfish-eu-central-1-prod-prisa.s3.amazonaws.com/public/I7MTIUSZB22PHS5HLBTWYS5SHQ.jpg'
image = get_image_from_file('images/role1.jpeg')

detect_labels(image)
# detect_labels_data(image)