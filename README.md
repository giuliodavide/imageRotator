Sometimes, when download images from the major images backup servers, I have problems with their metadatas,
in particular with their rotation, even if in the thumbnail all seems good.
This script allows you to rotate a list of images contained in a folder to fix this problem. I created this in order to rotate images
360 degrees, 'cause as I said all the images were already rotated in the exact direction and there were problem only with
their metadatas.

You can rotate the photos however you wanted, by running this script from terminal in this way:

**python main.py --folder /path/to/images/folder [--degree /degree/of/rotation]**

(the default value of degree is 360)