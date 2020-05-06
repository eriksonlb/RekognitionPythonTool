import boto3
from pprint import pprint
from image_helper import get_image_from_file, get_image_from_url

def recognize_celebrities_data(image_bytes):
    client=boto3.client('rekognition')
    response = client.recognize_celebrities(Image={'Bytes': image_bytes})
    pprint(response)

def recognize_celebrities(image_bytes):
    client=boto3.client('rekognition')
    response = client.recognize_celebrities(Image={'Bytes': image_bytes})
    faces = len(response['CelebrityFaces'])
    print(f'{faces} faces detected\n')
    for celebrity in response['CelebrityFaces']:
        name = celebrity['Name']
        confidence = celebrity['MatchConfidence']
        print (f'Name: {name}')
        print (f'Confidence: {confidence}%')
        for url in celebrity['Urls']:
            print (f'Link: {url}\n')
    

url = 'https://br.web.img3.acsta.net/c_215_290/pictures/18/06/29/00/35/0101925.jpg'
image = get_image_from_url(url)
recognize_celebrities(image)
# recognize_celebrities_data(image)