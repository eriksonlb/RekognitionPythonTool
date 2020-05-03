import boto3
from pprint import pprint
from image_helper import get_image_from_file, get_image_from_url

def detect_text(image_bytes):
    client=boto3.client('rekognition')
    response = client.detect_text(Image={'Bytes': image_bytes})
    textDetections = response['TextDetections']
    print ('Detected text\n----------')
    for text in textDetections:
        print ('Detected text:' + text['DetectedText'])
        print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
        print ('Id: {}'.format(text['Id']))
        if 'ParentId' in text:
            print ('Parent Id: {}'.format(text['ParentId']))
        print ('Type:' + text['Type'])
        print()
    return len(textDetections)

document = get_image_from_file('images/cnh.jpeg')
card = get_image_from_file('images/va.jpeg')
detect_text(card)