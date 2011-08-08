"""Yeah! The pictureMerger.py doesn't take pictures, or merge them, (at least
    at the moment) what it does do, is retrieve pictures from maps.google.com,
    and saves them as a handy-dandy file on your computer! """
import time
import converter
import os
import urllib2
import Image
from Tkinter import *
import tkFileDialog


frames = []
framedata = {}
final = None

def getFrame(url):
    """Pulls a frame from the google servers to a string object"""
    opener = urllib2.build_opener()
    page = opener.open(url)
    frame = page.read()
    return frame

def pieceTogether():
    final = Image.new("RGB",(tilesEast*256+tilesEast,tilesSouth*256+tilesSouth),"Black")
    stop=False
    for x in range(tilesEast):
        for y in range(tilesSouth):
            if (x,y) == furthest:
                stop = True
            newframe = Image.open(str(defaultPath)+"x"+str(originx+x)+" y"+str(originy+y)+" z"+str(zoomz)+".jpg")
            final.paste(newframe,(x*257,y*257))
            print "Combined: "+str(x)+", "+str(y)
            if stop==True:
                break
        if stop==True:
            break
    final.save(str(defaultPath)+"final"+str(NWcorner)+" z"+str(zoomz)+".jpg")
    print "Saved final image"

def megaImage():
    done=False
    paths = []
    root = Tk()
    try:
        while not done:
            newpath = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
            paths.append(newpath)
            getout = raw_input("Ctrl-C to finish")
    except KeyboardInterrupt:
        pass
    print paths
    zoom = raw_input("Zoom level")
    maxx,maxy,minx,miny = 0,0,0,0
    imglist = {}
    for directory in paths:
        filelist=os.listdir(directory)
        for path in filelist
            tempimg = Image.open(directory+path)
            info = path.split(" ")
            xvalue = info[0].strip("x")
            y
            imglist[path]={"Image":tempimg, "x":xvalue, "y":yvalue, "z":zvalue}

    
def savePicture(picture,filepath):
    """Print a saved picture"""
    """Note that the filepath on Windows is a bit buggy, and '\'s after the User
            account name need to by double slashes."""
    f = open(filepath,'wb')
    f.write(picture)
    f.close()
    """Note, if the file is corrupted it'll look like rubbish, be warned."""


"""Automates the system, ought to actually check how large each image is before
        throwing in a random number set..."""
print "Automatic Google Earth downloader"
print """Areas are defined by the NorthWest Corner, how many miles east and south
            and size and zoom levels 'Google Maps Defined'"""
NWcorner = raw_input("What are the latitude and longitude coordinates of your NW corner? ")
if NWcorner.lower() != "manual":
    NWlat,NWlon = NWcorner.split(",")
    NWlat,NWlon = float(NWlat),float(NWlon)
##distanceEast = float(raw_input("How many miles East do you want the selection to go? "))
##distanceSouth = float(raw_input("How many miles South do you want the selection to go? "))
tilesEast = int(raw_input("How many tiles to the East? "))
tilesSouth = int(raw_input("How many tiles to the South? "))
zoomlevel = int(raw_input(""""What is the zoom level you want? (Min 2: country sized,
Max 15: street block size) """))
if NWcorner.lower() == "manual":
    originx = int(raw_input("Originx: "))
    originy = int(raw_input("Originy: "))
    zoomz = zoomlevel
else:
    originx,originy,zoomz = converter.tile_info(NWlat,NWlon,zoomlevel)
defaultPath = str(raw_input("What is the folder you want to dump images in? "))
furthest = (0,0)



for etiles in range(tilesEast):
        for stiles in range(tilesSouth):
            curx = (originx+etiles)
            cury = (originy+stiles)
            try:
                pic = getFrame(("http://khm1.google.com/kh/v=89&x="+str(curx)+"&y="+str(cury)+"&z="+str(zoomz)+"&s=Ga"))
                savePicture(pic,str(defaultPath)+"x"+str(curx)+" y"+str(cury)+" z"+str(zoomz)+".jpg")
            except Exception as error:
                print error
                if "HTTP" in str(error):
                    print "Google bot exception, holding until proxy change..."
                    raw_input("Press and key (and enter) to continue ")
##                    f = open(str(defaultPath)+"x"+str(curx)+" y"+str(cury)+" z"+str(zoomz)+".jpg")
##                    f.close()
            print "x: "+str(etiles)+", y: "+str(stiles)
            furthest = (etiles,stiles)

        
    
pieceTogether()
