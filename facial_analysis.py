import boto3
from pprint import pprint
from image_helper import get_image_from_file, get_image_from_url

def facial_analysis(image_bytes):
    client=boto3.client('rekognition')
    face_resp = client.detect_faces(Image={'Bytes': image_bytes}, Attributes=['ALL'])
    print('\n\nFacial Labels:')
    faces = len(face_resp['FaceDetails'])
    print(f'{faces} face(s) detected:\n')
    for details in face_resp['FaceDetails']:
        # construct string by attributes
        formated_str = '   {gender} - age {lowage}-{highage},'

        # mustache and beard detection
        if details['Mustache']['Value'] and facedeets['Beard']['Value']:
            formated_str += ' with beard and mustache,'
        elif details['Mustache']['Value']:
            formated_str += ' with mustache,'
        elif details['Beard']['Value']:
            formated_str += ' with beard,'

        # Sunglasses/eyeglasses detection
        if details['Sunglasses']['Value']:
            formated_str += ' wearing sunglasses,'
        elif details['Eyeglasses']['Value']:
            formated_str += ' wearing glasses,'

        formated_str += ' looks {emotion}'

        print(
            formated_str.format(
                gender=details['Gender']['Value'],
                lowage=details['AgeRange']['Low'],
                highage=details['AgeRange']['High'],
                emotion=details['Emotions'][0]['Type'].lower()
            )
        )

image = get_image_from_file('images/team1.jpeg')
facial_analysis(image)