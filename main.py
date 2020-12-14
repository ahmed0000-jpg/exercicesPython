
# import Image and TAGS from pillow module
from PIL import Image
from PIL.ExifTags import TAGS

# Open the image that we want to get metadata from it using open("image path") function
my_image = Image.open("clav.jpg")

# extract exif data from image
exif_data = my_image.getexif()

# print tag start from 0 to 16 char for perfect format
for tagId in exif_data:
    # get the tag name
    tag = TAGS.get(tagId, tagId)
    data = exif_data.get(tagId)

    print(f"{tag:16}: {data}")
# as you can see all metadata information listed successfully as camera name, model, DateTimeOriginal