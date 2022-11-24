from skimage import io
import cv2
# loop over the image URLs
urls = [
	"https://pyimagesearch.com/wp-content/uploads/2015/01/opencv_logo.png",
	"https://pyimagesearch.com/wp-content/uploads/2015/01/google_logo.png",
	"https://pyimagesearch.com/wp-content/uploads/2014/12/adrian_face_detection_sidebar.png",
]
for url in urls:
	# download the image using scikit-image
	print ("downloading %s" % (url))
	image = io.imread(url)
	cv2.imshow("Incorrect", image)
	cv2.waitKey(0)