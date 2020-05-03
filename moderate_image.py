import boto3
from pprint import pprint
from image_helper import get_image_from_file, get_image_from_url

def moderate_image(image_bytes):
    client=boto3.client('rekognition')
    response = client.detect_moderation_labels(Image={'Bytes': image_bytes})
    print('Labels:')
    for label in response['ModerationLabels']:
        name = label['Name']
        confidence = label['Confidence']
        print(f'{name} : {round(confidence)}%')

# url = 'https://static.cdnlive.com.br/uploads/271/produto/15618447445128_zoom.jpeg'
url = 'https://trenditgh.com/wp-content/uploads/2020/04/screen-shot-2019-06-25-at-5-20-19-pm-1561497689.png'
image = get_image_from_url(url)
moderate_image(image)