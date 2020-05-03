import boto3
from pprint import pprint
from image_helper import get_image_from_file, get_image_from_url

def compare_faces_data(image_source, image_target):
    client = boto3.client('rekognition')
    response = client.compare_faces(SimilarityThreshold=80,
                                SourceImage={'Bytes': image_source},
                                TargetImage={'Bytes': image_target})
    pprint(response)

def compare_faces(image_source, image_target):
    client = boto3.client('rekognition')
    response = client.compare_faces(SimilarityThreshold=80,
                                SourceImage={'Bytes': image_source},
                                TargetImage={'Bytes': image_target})
    for faceMatch in response['FaceMatches']:
        similarity = faceMatch['Similarity']
        print(f'Matches with {round(similarity, 2)}% confidence')

url_img_src = 'images/eu.jpg'
url_img_target = 'images/role1.jpeg'

img_src = get_image_from_file(url_img_src)
img_target = get_image_from_file(url_img_target)

# compare_faces(img_src, img_target)
compare_faces_data(img_src, img_target)