import cv2
import numpy as np
a = int(input("Select 0 to highlight dark region selection \n Select 1 to highlight light region - "))
file_name = input("Enter the file name - ")
file_name1 = file_name.replace(".png","")
input_image_1 = cv2.imread(file_name)
cv2.imshow("Input",input_image_1)
cv2.waitKey()

# b = 1 when a =1 ; b = -1 when a = 0, b value used in nested for-loop to change comparision from '>' to'<' 
b = 2*a - 1

# Generate and save greyscale image
blue, green, red = input_image_1[:,:,0], input_image_1[:,:,1], input_image_1[:,:,2]
Average_Gray = np.uint8(0.33*blue + 0.33*green + 0.33*red)
cv2.imshow("Greyscale",Average_Gray)
cv2.waitKey()
cv2.imwrite(f"{file_name1}_Greyscale.png",Average_Gray)
i, j = np.shape(Average_Gray)

# The part that I enjoyed writing

# Initialize output image to original image
red = input_image_1

# Take black canvas and add white pixels and save these to output as red if we want to highlight lighter areas
# Take white canvas and add black pixels and save these to output as red if we want to highlight darker areas
# By doing so, we can create both the binary image and highlighted image within the same loop 
black_white = 255*(np.ones([i,j]) - a)

for ii in range(0,i):
    for jj in range(0,j):
        # Multiplying by b on LHS to invert comparision from > to < when b is negative!!!
        # check pixel strength > 70 when highlighting light areas and pixel strength < 170 when highlighting dark area
        if b*Average_Gray[ii,jj]>170*b - 100*a:
            black_white[ii,jj] = a*255
            red[ii,jj] = [0, 0, 255]

cv2.imshow("Binary",black_white)
cv2.waitKey()
cv2.imwrite(f"{file_name1}_Binary.png",black_white)
cv2.imshow("Output",red)
cv2.waitKey()
cv2.imwrite(f"{file_name1}_Output.png",red)

