Required packages:
	pandas        - For readind data files
	opencv-python - For reading the images
	numpy 	      - For easy computation
	matplotlib    - For displaying the graphs
	heapq     - For selecting K minimum distances 
	sklearn   - For splitting the data into 60:40 ratio

Input:
	titanic.csv

Scaling the data:
	Passenger Id doesn't give any information for classification 
	Gender values changed to numerical values (replaced male with '0' and female with '1')
	Missing age values replaced with Mean of the age
	Embarked values ('S','Q','C') with (0,1,2) 

Distance calculation:
	For numerical features - euclidean distance 
	For nominal features like (cabin) - hamming distance

Data distribution :
	size of Data =  231
	size of train_data =  138
	size of test_data =  93

Selecting K min neighbors:
	By using heaps we can select K minimum values with K log n time.
	Finally, calculated accuracy with predicted class and actual class

Observation:
	For K =[3,5,13,15,21,25] i got maximum accuracy


