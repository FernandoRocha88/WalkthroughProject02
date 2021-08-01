
import streamlit as st
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

def PredictionEvaluation(X,y,pipeline,LabelsMap):

  prediction = pipeline.predict(X)

  Map = list() 
  for key, value in LabelsMap.items():
    Map.append( str(key) + ": " + value)

  st.write('#### Confusion Matrix')
  st.code(pd.DataFrame(confusion_matrix(y_true=prediction, y_pred=y),
        columns=[ ["Actual " + sub for sub in Map] ], 
        index= [ ["Prediction " + sub for sub in Map ]]
        ))



  st.write('#### Classification Report')
  st.code(classification_report(y, prediction),"\n")




def PerformanceTrainTestSet(X_train,y_train,X_test,y_test,pipeline,LabelsMap):
  st.write("* Train Set")
  PredictionEvaluation(X_train,y_train,pipeline,LabelsMap)

  st.write("* Test Set")
  PredictionEvaluation(X_test,y_test,pipeline,LabelsMap)