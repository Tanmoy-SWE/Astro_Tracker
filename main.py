#Import required libraries:
import nasapy
import os
from datetime import datetime, timedelta
import urllib.request
from IPython.display import Image,display,Audio
from gtts import gTTS
from pandas import DataFrame
#Initialize Nasa class by creating an object:

k = "523p5hPYHGzafYGLCkqa54kKMTV2vbP0XcPxkcLm"
nasa = nasapy.Nasa(key = k)

#Get today's date in YYYY-MM-DD format:

d = datetime.today().strftime('%Y-%m-%d')
yesterday = datetime.today() - timedelta(days=1)
yesterday.strftime('%Y-%m-%d')
#Get the image data:

apod = nasa.picture_of_the_day(date=d, hd=True)
apodYesterday = nasa.picture_of_the_day(date=yesterday, hd=True)

# POINT A:
# Check the media type available:
if (apod["media_type"] == "image"):

    # POINT B:
    # Displaying hd images only:
    if ("hdurl" in apod.keys()):

        # POINT C:
        # Saving name for image:
        title = d + "_" + apod["title"].replace(" ", "_").replace(":", "_") + ".jpg"

        # POINT D:
        # Path of the directory:
        image_dir = "./Astro_Images"

        # Checking if the directory already exists?
        dir_res = os.path.exists(image_dir)

        # If it doesn't exist then make a new directory:
        if (dir_res == False):
            os.makedirs(image_dir)

        # If it exist then print a statement:
        else:
            print("Directory already exists!\n")

        # POINT E:
        # Retrieving the image:
        urllib.request.urlretrieve(url=apod["hdurl"], filename=os.path.join(image_dir, title))

        # POINT F:
        # Displaying information related to image:

        if ("date" in apod.keys()):
            print("Date image released: ", apod["date"])
            print("\n")
        if ("copyright" in apod.keys()):
            print("This image is owned by: ", apod["copyright"])
            print("\n")
        if ("title" in apod.keys()):
            print("Title of the image: ", apod["title"])
            print("\n")
        if ("explanation" in apod.keys()):
            print("Description for the image: ", apod["explanation"])
            print("\n")
        if ("hdurl" in apod.keys()):
            print("URL for this image: ", apod["hdurl"])
            print("\n")

        # POINT G:
        # Displaying main image:
        display(Image(os.path.join(image_dir, title)))

        # Point H:
        # Text to Speech Conversion:
        # Take input from user:
        print("\n")
        choice = input("Press * to hear the audio explanation : ")
# POINT I:
# If media type is not image:
else:
    print("Sorry, Image not available!")

if (apodYesterday["media_type"] == "image"):

    # POINT B:
    # Displaying hd images only:
    if ("hdurl" in apod.keys()):

        # POINT C:
        # Saving name for image:
        title = d + "_" + apodYesterday["title"].replace(" ", "_").replace(":", "_") + ".jpg"

        # POINT D:
        # Path of the directory:
        image_dir = "./Astro_Images"

        # Checking if the directory already exists?
        dir_res = os.path.exists(image_dir)

        # If it doesn't exist then make a new directory:
        if (dir_res == False):
            os.makedirs(image_dir)

        # If it exist then print a statement:
        else:
            print("Directory already exists!\n")

        # POINT E:
        # Retrieving the image:
        urllib.request.urlretrieve(url=apod["hdurl"], filename=os.path.join(image_dir, title))

        # POINT F:
        # Displaying information related to image:

        if ("date" in apodYesterday.keys()):
            print("Date image released: ", apodYesterday["date"])
            print("\n")
        if ("copyright" in apodYesterday.keys()):
            print("This image is owned by: ", apodYesterday["copyright"])
            print("\n")
        if ("title" in apodYesterday.keys()):
            print("Title of the image: ", apodYesterday["title"])
            print("\n")
        if ("explanation" in apodYesterday.keys()):
            print("Description for the image: ", apodYesterday["explanation"])
            print("\n")
        if ("hdurl" in apodYesterday.keys()):
            print("URL for this image: ", apodYesterday["hdurl"])
            print("\n")

        # POINT G:
        # Displaying main image:
        display(Image(os.path.join(image_dir, title)))

        # Point H:
        # Text to Speech Conversion:
        # Take input from user:
        print("\n")
        choice = input("Press * to hear the audio explanation : ")

# POINT I:
# If media type is not image:
else:
    print("Sorry, Image not available!")