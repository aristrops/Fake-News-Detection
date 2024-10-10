# Fake-News-Detection
Analysis a text dataset through NLP techniques and development of three models for  detecting fake news in newspaper articles.

We mainly used Colab PRO to create and run the code. The notebook has been run from start to finish and you can see the results of all the cells. 

We attach a folder "NLP", which contains all the useful files necessary to rerun the code. In order to use it correctly on Colab, you should upload this folder on your personal Drive, so that the paths that we have created may work correctly.
The folder is composed of several files:
-"Final_dataset.csv": this is the final dataset with the columns we created during the projects, and that will be exploited in the majority of the code
-"DatasetFeatures.csv": this is a particular dataset used for the SVM analysis, which is composed of several additional features, that have been divided from the comprehensive one to save some space and avoid having a single large file
-"code": this is a folder that contains the whole framework necessary to perform the sentiment analysis
-"dataset_sent": this folder contains the datasets generated from the sentiment analysis, in particular a comprehensive one ("sentimentAnalysis.csv") and one for each component ("arousal.csv", "dominance.csv", "valence.csv")

Please note that the original dataset that we used is not provided as it would be redundant, given that the first part of our analysis involved the concatenation of the original files and the addition of the "label" column, plus the preprocessing part. For this reason, you won't be able to run many cells of the code, as they require the original datasets that we used. A "NOTE" has been added to mark all the cells that cannot be run or that we suggest not to run, as they are strongly time consuming: the results of these cells can all be found in the datasets we provided and, when possible, an example on a small portion of the dataset is provided. 

Moreover, it is worth mentioning that an elevated RAM is required: we used Colab PRO and we ran the notebooks separately, so it has not been an issue for us, but it may be if you use the free version of Colab. In order to partially avoid this problem, we divided the sections so that they can be run independently from one another, so we suggest that, if you have less than 51GB RAM available, you disconnect the runtime after finishing the run of each section. At the beginning of each one, the useful datasets are reloaded, so that you can start running from there and clear the memory. 
You should be able to run the notebook in every part in this way, except for the "Recurrent Neural Network" section: by nature they exploit an elevated space, so you may still have some issues running it if you use the free version of Colab. However, we ran the whole code so that you are able to clearly see the results of that section as well, and if you want to rerun it you are free to run the notebook on your personal machine, just note that you may have to change something in the way you upload the datasets. We apologize for this issue. 

Also, please note that the results you find in the code may slightly differ from the ones we included in the report, in terms of accuracy and confusion matrices, and this is due to the fact that we rerun our code several times.  
