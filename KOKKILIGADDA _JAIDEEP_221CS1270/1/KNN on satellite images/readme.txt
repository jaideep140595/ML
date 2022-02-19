Required packages:

	opencv-python - For reading the images
	numpy 	      - For easy computation
	matplotlib    - For displaying the graphs
	heapq     - For selecting K minimum distances 
	sklearn   - For splitting the data into 60:40 ratio

Input images:
	"1.jpg"
	"2.jpg"
	"3.jpg"
	"4.jpg" 

Implementation of KNN classification using satellite images
	Total number of samples, selected from satellite images, are 280. 
	'0' is assigned to river data and '1' is to non-river data
	After spliting the data into train and test sets using 60:40 ratio, each set contains 168 and 112 samples respectively.(Data is randomly shuffled every time and training data and test data is taken in ratio 60:40)
	Find ecludian distance from each test sample to all training samples and sorted the distances in increasing order
	Select K minimum distances and add the most probable class to predicted class (For finding K minimum distances, used heaps to reduce the time complexity)
	Finally, calculated accuracy with predicted class and actual class

Observation:
	Got maximum accuracy at K=1

Run:
	Open 221CS1270.ipynb file with jupyter and Run every section to get desired output