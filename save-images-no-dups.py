import json
import urllib.request
from PIL import Image
from PIL import ImageOps


# This gets all the images from the file - saves them, and flips them
with open('ims.json') as data_file:    
    data = json.load(data_file)
    i = 0
    for image in data:
        i += 1
        print(image['Label'])
        print("")
        # If there is an image..
        if len(image['Label']) > 0:
            
            # Save the image
            imageURL = image['Labeled Data']
            img = urllib.request.urlretrieve(imageURL, f"images/{i}.jpeg")
            # ensure no RGBA sneaks in...
            img = Image.open(f"images/{i}.jpeg").convert('RGB').save(f"images/{i}.jpeg")


            # # then save the label
            segmented = image['Label']['objects'][0]['instanceURI']
            img = urllib.request.urlretrieve(segmented, f"masks/{i}.png")
            img = Image.open(f"masks/{i}.png").convert('RGB')
            img.save(f"masks/{i}.png")
           

