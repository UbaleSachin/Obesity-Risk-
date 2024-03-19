# Obesity-Risk-
Goal : The goal of this project is to use various factors to predict obesity risk in individual's,which
      is related to cardiovascular disease.

About Dataset: The data consist of the estimation of obesity levels in people from the countries of Mexico, Peru and Colombia, 
               with ages between 14 and 61 and diverse eating habits and physical condition.

Projetc Description : 
   1.The application takes features related to eating habits=
         1.Frequent consumption of high caloric food, 
         2.Number of main meals,
         3.Consumption of food between meals, 
         4.Consumption of water daily,
         5.Consumption of alcohol. 
   2.The attributes related with the physical condition are: 
       1.Calories consumption monitoring, 
       2.Physical activity frequency, 
       3.Time using technology devices, 
       4.Transportation used
   3.And predicts the Obesity level:
       1.Underweight Less than 18.5
       2.Normal 18.5 to 24.9
       3.Overweight 25.0 to 29.9
       4.Obesity I 30.0 to 34.9
       5.Obesity II 35.0 to 39.9
       6.Obesity III Higher than 40
   4.The higher your BMI, the greater is your risk of developing obesity-related health problems

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
   2. dvc repro / for without dvc use python main.py
