# Obesity-Risk-
Goal : The goal of this project is to use various factors to predict obesity risk in individual's,which
      is related to cardiovascular disease.

About Dataset: The data consist of the estimation of obesity levels in people from the countries of Mexico, Peru and Colombia, 
               with ages between 14 and 61 and diverse eating habits and physical condition.

Projetc Description : 
   The application takes features related to eating habits:
                        Frequent consumption of high caloric food, 
                        Number of main meals, 
                        Consumption of food between meals, 
                        Consumption of water daily,
                        Consumption of alcohol. 
                     The attributes related with the physical condition are: 
                        Calories consumption monitoring, 
                        Physical activity frequency, 
                        Time using technology devices, 
                        Transportation used
                     And predicts the Obesity level:
                        Underweight Less than 18.5
                        Normal 18.5 to 24.9
                        Overweight 25.0 to 29.9
                        Obesity I 30.0 to 34.9
                        Obesity II 35.0 to 39.9
                        Obesity III Higher than 40
                     The higher your BMI, the greater is your risk of developing obesity-related health problems

Dependencies:
   1. pandas
   2. numpy
   3. matplotlib
   4. scikit-learn
   5. seaborn
   6. xgboost
   7. catboost
   8. flask
   9. dvc
   10. pyYAML
   11. tqdm
   12. python-box[all]==7.1
   13. ensure
   14. mlflow
To install dependencies run
   pip install -r requirements.txt

To run on local machine use command
   1. dvc init
   2. dvc repro
or
   1. python main.py
