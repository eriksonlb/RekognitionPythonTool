import boto3
from pprint import pprint
import image_helpers

# AWS configuration
access_id = 'AKIA6MZTIFV47X6IQOUP'
access_key = 'QpuB9w12e83JXuO9a9nqTC6+cOTC3YX8N+Syb+3k'
client = boto3.client('rekognition', 
        region_name='us-west-1', 
        aws_access_key_id=access_id,
        aws_secret_access_key= access_key)
    




def get_labels():
    labels_resp = client.detect_labels(Image={'Bytes': imagebytes}, MinConfidence=50)
    # pprint(labels_resp)
    print('\n\nLabels:')
    for label in labels_resp['Labels']:
        label_name = label['Name']
        label_confidence = label['Confidence']
        print(f' {label_name}  --  {round(label_confidence, 2)}%')

def get_facial_labels():
    face_resp = client.detect_faces(Image={'Bytes': imagebytes}, Attributes=['ALL'])
    # pprint(face_resp)
    print('\n\nFacial Labels:')
    faces = len(face_resp['FaceDetails'])
    print(f'Foram encontradas {faces} face(s):\n')
    for details in face_resp['FaceDetails']:
        # construct string by attributes
        formated_str = '   {gender} age {lowage}-{highage},'

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

def get_celebs_info():
    resp = client.recognize_celebrities(Image={'Bytes': imagebytes})
    # pprint(rekresp['CelebrityFaces'])
    for face in resp['CelebrityFaces']:
        name = face['Name']
        confidence = face['MatchConfidence']
        url = face['Urls']
        url = str(url)
        print(f'Name: {name}, Confidence: {round(confidence, 2)}%, URL: {url}')
        
# Imagens teste
# imageurl = 'https://cdn-ofuxico.akamaized.net/img/upload/noticias/2020/03/18/terry-crews_373709_36.jpg'
imageurl = 'https://www.researchgate.net/profile/Suzy_Lidstrom/publication/323289653/figure/fig7/AS:596135865499654@1519141274384/Kip-Thorne-and-Stephen-Hawking-with-actors-of-the-movie-Interstellar-David-Gyasi-Anne.png'

# imagename = 'images/team1.jpeg'
# imagename = 'images/role1.jpeg'
# imagename = 'images/kid_and_cat.jpeg'
# imagename = 'images/dn_outdoor.jpg'
imagename = 'images/bad_guy.jpg'

# Convert image in bytecode
# imagebytes = image_helpers.get_image_from_file(imagename)
imagebytes = image_helpers.get_image_from_url(imageurl)

# get_labels()
# get_facial_labels()
get_celebs_info()