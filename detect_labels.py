import boto3
from pprint import pprint
from image_helper import get_image_from_file, get_image_from_url

def detect_labels_data(image_bytes):
    client = boto3.client('rekognition')
    response = client.detect_labels(Image={'Bytes': image_bytes}, MinConfidence=50)
    pprint(response)

def detect_labels(image_bytes):
    client = boto3.client('rekognition')
    response = client.detect_labels(Image={'Bytes': image_bytes}, MinConfidence=50)
    print('\n\nLabels:')
    for label in response['Labels']:
        label_name = label['Name']
        label_confidence = label['Confidence']
        print(f' {label_name}  --  {round(label_confidence, 2)}%')


url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Av_Francisco_Glic%C3%A9rio_-_Campinas_SP_-_panoramio.jpg/1200px-Av_Francisco_Glic%C3%A9rio_-_Campinas_SP_-_panoramio.jpg'
image = get_image_from_file('images/role1.jpeg')

detect_labels(image)
# detect_labels_data(image)