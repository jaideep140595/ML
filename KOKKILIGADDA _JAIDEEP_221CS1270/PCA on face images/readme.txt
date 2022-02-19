Required packages:
	pandas        - For reading data files
	opencv-python - For reading the images
	numpy 	      - For easy computation
	matplotlib    - For displaying the graphs
	sklearn   - For splitting the data into 60:40 ratio

Input images:
	"face_data"

Data distribution :
	size of Data =  400 images
	size of train_data =  240 images
	size of test_data =  160 images

Observation:
	After applying pca, i select best 200 features in 10302 features
	Data reduced from 10302*240 to 200*240

Accuracy:
	From k value 1 to 75 acuuracy is increasing quickly
	After reaching K value 75 accuracy is slightly increasing
	and maximum accuracy is 0.95

Run:

Open 221CS1270_ML_Assignment2.ipynb file with jupyter and Run every section to get desired output