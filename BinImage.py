# Codes that convert image into Array[] value ,
# this array can be used for different action in future
# ihsan Ullah khan M.Sc Electronics 2003, Peshawar, KPK , Pakistan
from PIL import Image
# install PILLOW package
from numpy import array
#install numpy Packge
# put address of image & type  that you want to make array[] value of picturesor image
im_1 = Image.open("C:\\Users\\ihsan\\Desktop\\Test\\test1.jpg")
# Print array value of Picture #
print("Pic_Array ",array(im_1))
# end of codes
