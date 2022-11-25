from typing import Literal
from PIL import Image
import face_recognition
import os
import cv2

boolean = True
count = 0

frames = os.listdir('/home/yasmim-lapisco/Documentos/frames/framesVIP 5220 SD IR/record_11')

for i in frames:
    image = face_recognition.load_image_file(f"/home/yasmim-lapisco/Documentos/frames/framesVIP 5220 SD IR/record_11/{i}")
    face_locations = face_recognition.face_locations(image)
    #print(face_locations)


    for face_location in face_locations:

        # printa a localização de cada imagem por frame
        top, right, bottom, left = face_location
        #print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
         # print(pil_image)
        pil_image.save(f'/home/yasmim-lapisco/Documentos/frames/output/figurinhas_{count}.png')
        count+=1
print(count)

        