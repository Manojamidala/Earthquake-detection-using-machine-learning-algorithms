# The Cavalcade of Immaculate and Disparate Algorithms for Detecting Distracted Earthquakes Employing Machine Learning.
## Abstract
An Earthquake is the sudden shaking of the surface of the earth resulting from sudden release of energy in the Lithosphere. Earthquake detection using machine learning is a promising approach to improving the speed and accuracy of earthquake detection. Machine learning algorithms use statistical models to analyze seismic data and identify patterns associated with earthquakes. The process of earthquake detection using machine learning involves collecting seismic data from seismometers and extracting relevant features from the data. The features extracted from the seismic data are used to train machine learning models such as decision tree, KNeighborsClassifier , Support Vector Machines , and Random Forest Classifier to identify patterns in the seismic waves associated with earthquakes. Once the models are trained, they can be used for earthquake detection.
## Workflow:
![image](https://user-images.githubusercontent.com/88728002/231971025-76c51414-bf4c-4bbc-9ada-d81b32a03fad.png)

The Schematic Representation of Workflow Process

## System Requirements
1.	Hardware Requirements 
MINIMUM (Required for Execution)	MY SYSTEM (Development)
System	Pentium IV 2.2 GHz	i3 Processor 5th Gen
Hard Disk	20 Gb	500 Gb
Ram	1 Gb	4 Gb

2.	Software Requirements 
Operating System	Windows 10/11
Development Software	Python 3.10
Programming Language	Python
Domain	Machine Learning
Integrated Development Environment (IDE)	Visual Studio Code, Google Colab

## Results And Analysis:
Following results were observed after executing the python code:
In this section, results are analysed using classification technique Decision tree, SVM, K-Neighbour’s classifier and Random Forest Algorithms. The classification technique implementation was performed using Matplotlib Library. Here the dataset contains various attributes of earthquake, depth, magnitude, longitude, latitude, here we divided the data into two parts which consists of training data and other is validating data,
With the given training data, we trained a Decision tree, SVM model, KN classifier model and Random Forest model. Then using validating data, we validated the models and plotted a confusion matrix and found out the 93.07% accuracy through SVM model, 92.30% accuracy through K-Neighbours classifier model and 94.23% accuracy through Decision Tree classifier model and 97.69% accuracy for the Random Forest classifier.
By comparing the Decision tree SVM, Neighbour’s classifier, Random Forest algorithms Random Forest gives the better accuracy rate of 97.


![table](https://user-images.githubusercontent.com/88728002/231972167-388d3204-2994-4133-9068-d9da9b61b17c.png)
Table.1: The Comparisons of the above Algorithms on Various Factors


![image](https://user-images.githubusercontent.com/88728002/231972599-c2bef7e8-700f-45ab-a5c4-d83d8da309b2.png)
The Schematic Representation of Data Visualization of Corresponding Algorithms

## Output:
It emphasizes that the use of earthquake detection and random forest algorithms to predict earthquake magnitudes. It suggests that using a random forest algorithm for earthquake detection gives high accuracy, and that prediction can be done using attributes such as longitude, latitude, depth, cdi, mmi, sig, dmin, nst, and gap.
By using machine learning technique random forest, we can accurately predict the magnitude of an earthquake using various attributes of the earthquake. This could be a valuable tool for disaster management agencies and first responders who need to quickly assess the potential impact of an earthquake and take appropriate action to minimize damage and loss of life.

            enter the logitude 159.0270
            enter the latitude -54.1325
            enter depth 10.000
            enter cdi 2
            enter mmi 5 
            enter sig 733
            enter dmin 0.371
            enter nst 127
            enter gap 45.0
            low magnitude earthquakes


## Conclusion:
Based on the evaluation of four machine learning algorithms, namely Decision Tree Classifier, KNeighborsClassifier, SVC, and Random Forest Classifier, it can be concluded that all models have performed well in detecting earthquakes. Among all the algorithms, the Random Forest Classifier algorithm achieved the highest accuracy score of 0.976923, which is the best performance compared to the other models. The Decision Tree Classifier, KNeighborsClassifier, and SVC algorithms also performed well, with accuracy scores of 0.942308, 0.923077, and 0.930769, respectively. Moreover, all the models have performed well in terms of precision, recall, and F1-score. These performance metrics are essential for earthquake detection as it requires accurate and reliable predictions to avoid false positives and false negatives. In conclusion, the Random Forest Classifier algorithm is the best model for earthquake detection based on the given dataset. However, other algorithms such as Decision Tree Classifier, K-Neighbour’s Classifier, and SVC can also be used as they have also shown good performance.



          

          


 
