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
            # import code; code.interact(local=dict(globals(), **locals()))

            img = urllib.request.urlretrieve(imageURL, f"images/{i}.jpeg")
            
            # then flip it...
            im = Image.open(f"images/{i}.jpeg")
            im = ImageOps.mirror(im)
            im = im.convert("RGB")
            im.save(f"images/{i}m.jpeg")
            im = ImageOps.flip(im)
            im.save(f"images/{i}f.jpeg")
            im = ImageOps.mirror(im)
            im.save(f"images/{i}fm.jpeg")

            # # then save the label
            segmented = image['Label']['objects'][0]['instanceURI']
            # import code; code.interact(local=dict(globals(), **locals()))

            img = urllib.request.urlretrieve(segmented, f"masks/{i}.png")
            # then flip it...
            im = Image.open(f"masks/{i}.png")
            im = ImageOps.mirror(im)
            im.save(f"masks/{i}m.png")
            im = ImageOps.flip(im)
            im.save(f"masks/{i}f.png")
            im = ImageOps.mirror(im)
            im.save(f"masks/{i}fm.png")

            # import code; code.interact(local=dict(globals(), **locals()))
