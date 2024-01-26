# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 21:11:00 2023

@author: 91959
"""
import streamlit as st

# Simulating a database
user_password = "mypassword"

# Function to validate the password
def validate_password(password):
    return password == user_password

# Function to handle the login process
def handle_login(password):
    if validate_password(password):
        st.session_state.is_authenticated = True
    else:
        st.error("Invalid password. Please try again.")

# Main function
def main():
    st.title("Login Authentication")

    # Check if the 'is_authenticated' attribute is present in the st.session_state
    if "is_authenticated" not in st.session_state:
        st.session_state.is_authenticated = False

    # If the user is not authenticated, display a login form
    if not st.session_state.is_authenticated:
        st.subheader("Please enter your password to login:")
        password = st.text_input("Password", type="password")
        submit_button = st.button("Submit")

        if submit_button:
            handle_login(password)
    else:
        st.success("You are successfully logged in.")

if __name__ == "__main__":
    main()


diabetes_model = pickle.load(open('C:/Users/91959/Desktop/PROJECT/ELITE/MULTIPLE DISEASE PREDICTION/saved models/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('C:/Users/91959/Desktop/PROJECT/ELITE/MULTIPLE DISEASE PREDICTION/saved models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/91959/Desktop/PROJECT/ELITE/MULTIPLE DISEASE PREDICTION/saved models/parkinsons_model.sav','rb'))

breast_cancer_model=joblib.load(open('C:/Users/91959/Desktop/PROJECT/ELITE/MULTIPLE DISEASE PREDICTION/saved models/breast_cancer_model.sav','rb'))

lung_cancer_model=pickle.load(open('C:/Users/91959/Desktop/PROJECT/ELITE/MULTIPLE DISEASE PREDICTION/saved models/lung_cancer_model.sav','rb'))
with st.sidebar:

   selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Breast Cancer disease Prediction',
                           'Lung Cancer Prediction'
                          ],
                          icons=['activity','heart','person','activity','lungs'],
                          default_index=0)
    
    # Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction')
    
    
    # getting the input data from the user 
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1: 
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'Sorry!! You have diabetes,Take Care!'
        else:
          diab_diagnosis = 'NO !! You are Healthy!!'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex')
        
    with col3:
        cp = st.number_input('Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'Sorry,You might have a Heart disease!! Kindly take care of yourself'
          
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "Sorry!! You might have a parkinsons disease.Take Care"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    

    # Breast Cancer Prediction Page
if (selected == 'Breast Cancer disease Prediction'):
    
    # page title
    st.title('Breast Cancer Prediction')
    
    
    # getting the input data from the user 
    col1, col2, col3,col4 = st.columns(4)
          
   
    
    with col1:
        texture_mean = st.number_input('texture_mean')
    
    with col2: 
        perimeter_mean = st.number_input('perimeter_mean')
    
    with col3:
        area_mean = st.number_input('area_mean')
    
    with col4:
       smoothness_mean = st.number_input('smoothness_mean')
    
    with col1:
        compactness_mean = st.number_input('compactness_mean')
    with col2:
        concavity_mean = st.number_input('concavity_mean')
    with col3:
        concave_points_mean = st.number_input('concave_points_mean')
    with col4:
        symmetry_mean = st.number_input('symmetry_mean')
    with col1:
        fractal_dimension_mean = st.number_input('fractal_dimension_mean')
    with col2:
        radius_se = st.number_input('radius_se')
    with col3:
        texture_se = st.number_input('texture_se')
    with col4:
        perimeter_se= st.number_input('perimeter_se')
    with col1:
        area_se = st.number_input('area_se')
    with col2:
        smoothness_se = st.number_input('smoothness_se')
    with col3:
        compactness_se = st.number_input('compactness_se')
    with col4:
        concavity_se = st.number_input('concavity_se')
    with col1:
        concave_points_se = st.number_input('concave points_se')
    with col2:
        symmetry_se = st.number_input('symmetry_se')
    with col3:
        fractal_dimension_se = st.number_input('fractal_dimension_se')
    with col4:
        radius_worst= st.number_input('radius_worst')
    with col1:
        texture_worst = st.number_input('texture_worst')
    with col2:
        perimeter_worst = st.number_input('perimeter_worst')
    with col3:
        area_worst = st.number_input('area_worst')
    with col4:
        smoothness_worst = st.number_input('smoothness_worst')
    with col1:
        compactness_worst = st.number_input('compactness_worst')
    with col2:
        concavity_worst = st.number_input('concavity_worst')
    with col3:
        concave_points_worst = st.number_input('concave points_worst') 
    with col4:
        symmetry_worst = st.number_input('symmetry_worst')
    with col1:
        fractal_dimension_worst = st.number_input('fractal_dimension_worst')
    with col2:
        radius_mean=st.number_input('radius_mean')

    
    
    # code for Prediction
    breastcr_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Breast Cancer Test Result'):
        breastcr_prediction = breast_cancer_model.predict([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]])
        
        if (breastcr_prediction[0] == 1):
          breastcr_diagnosis = 'Sorry!! You have Breast Cancer,Take Care!'
        else:
          diab_diagnosis = 'NO !! You are Healthy!!'
        
    st.success(breastcr_diagnosis)

    


if (selected == 'Lung Cancer Prediction'):
    
    # page title
    st.title('Lung Cancer Prediction')
    
    
    # getting the input data from the user 
    col1, col2, col3,col4 = st.columns(4)
          
   
    
    
    with col1:
        YELLOW_FINGERS= st.number_input('YELLOW_FINGERS')
    with col2:
        ANXIETY = st.number_input('ANXIETY')
    with col3:
        PEER_PRESSURE = st.number_input('PEER_PRESSURE')
    with col4:
        CHRONIC_DISEASE = st.number_input('CHRONIC_DISEASE')
    with col1:
        FATIGUE = st.number_input('FATIGUE')
    with col2:
        ALLERGY = st.number_input('ALLERGY')
    with col3:
        WHEEZING = st.number_input('WHEEZING')
    with col4:
        ALCOHOL = st.number_input('ALCOHOL')
    with col1:
        COUGHING= st.number_input('COUGHING')
    with col2:
        SHORTNESS_OF_BREATH = st.number_input('SHORTNESS_OF_BREATH')
    with col3:
        SWALLOWING_DIFFICULTY = st.number_input('SWALLOWING_DIFFICULTY')
    with col4:
        CHEST_PAIN= st.number_input('CHEST_PAIN')
    
    
    
 

    lung_diagnosis = ''

# creating a button for Prediction
    if st.button('Lung Cancer Test Result'):
    # Assuming your input data is stored in a list (modify accordingly)
     input_data = [YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE, ALLERGY, WHEEZING,ALCOHOL,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]

   

    # Make predictions using the loaded model
     input_data_array = np.array(input_data)

# Reshape the array
     reshaped_input_data = input_data_array.reshape(1, -1)

# Make predictions using the loaded model
     lung_cancer_prediction = lung_cancer_model.predict(reshaped_input_data)

# Check the result and set the diagnosis
     if lung_cancer_prediction[0] == 1:
      lung_diagnosis = 'Sorry!! You have Lung Cancer, Take Care!'
     else:
      lung_diagnosis = 'NO!! You are Healthy!!'

    # Display the diagnosis result
    st.success(lung_diagnosis)
import streamlit as st



