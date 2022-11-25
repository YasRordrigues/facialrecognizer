import cv2
import os



# Load the cascade
face_cascade = cv2.CascadeClassifier('/home/yasmim-lapisco/Downloads/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')

#save .png in the list    
file_list = [] 
   

path = '/home/yasmim-lapisco/Documentos/frames/framesVIP 3220 B/record_11'
os.chdir(path)
    
for file in os.listdir(path):
    if file.endswith(".png"):
        file_list.append(file)

list_faces = []

#pass to gray
count = 0
for file in file_list:
    img = cv2.imread(file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    
        
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        i = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        

        cv2.imwrite(f'/home/yasmim-lapisco/Documentos/frames/output/figurinhas_{count}.png', img)
    
        
        count += 1


cv2.waitKey()

#print the quantity
print(count)
