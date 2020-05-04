import boto3
from pprint import pprint
from image_helper import get_image_from_file, get_image_from_url

def detect_text_data(image_bytes):
    client=boto3.client('rekognition')
    response = client.detect_text(Image={'Bytes': image_bytes})
    pprint(response)

def detect_text(image_bytes):
    client=boto3.client('rekognition')
    response = client.detect_text(Image={'Bytes': image_bytes})
    textDetections = response['TextDetections']
    for text in textDetections:
        print ('Detected text:' + text['DetectedText'])
        print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
        print()
    return len(textDetections)

document = get_image_from_file('images/cnh.jpg')
card = get_image_from_file('images/card.png')
detect_text(card)
# detect_text_data(document)