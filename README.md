YouTube RPM Predictor

— a from-scratch linear regression model that predicts YouTube RPM ($ per 1000 views) based on video niche, audience country, duration, and retention.



Used features:
- country: mapped to a CPM tier (1=high, 2=medium, 3=low) since advertiser demand and ad rates vary heavily by country
- duration: duration of the full video
- retention: % of the video actually watched (watched duration ÷ total duration) | higher retention signals more engaged viewers
- niche: [tech, gaming, finance, education], encoded numerically — advertiser CPM differs a lot by content category | tech pays more than gaming


Output:
- RPM (revenue per mille): predicted revenue in $ per 1000 views


Dataset 
- The model is trained on "youtube_data.txt", AI-generated dataset of 1500 examples with columns: country, duration, retention, niche, rpm.
Since the data is synthetic rather than real-world YouTube analytics, the learned relationships may not reflect actual RPM patterns.


Functions:
- load_data: loads the data from "youtube_data.txt" & normalizes the data
- compute_modelOutput: computes model's output using linear regression equation
- compute_Cost: computes cost function 
- compute_gradient: computes derivative of w & bias continously and returns dw,db to be used in gradeint_descent()
- gradeint_descent: runs gradient descent for "iters" iterations updating w and b using learning rate "alpha", and returns the final values


How it works?
> calling load_data() and normalizing data using z-score 
> setting inital w,b 
> gets inputs from the user 
> calculates w_final, b_final using gradeint_descent() 
> normaling new X 
> computing the prediction using the linear regression equation(compute_modelOutput)
> prints the prediction


Why normalizing?
- Data range varies between each other. country(1 - 3), duration(3 - 200), retention(0 - 100)which makes gradient descent converge unevenly.
- Z-score normalization scales everything to a similar range so the model trains faster and more reliably.


Why log-transform the target?
- RPM values are skewed (mostly low values with a few high outliers) and must always stay positive — but plain linear regression can output negative numbers.
- Training on log(RPM) and exponentiating the prediction back keeps outputs positive and helps the model handle the skew better.


How to run it
in bash 'python main.py'

You'll be prompted for:
- Niche (tech / gaming / finance / education)
- Country
- Video duration (minutes)
- Retention (%)

The script trains the model on youtube_data.txt, then prints the predicted RPM per 1000 views.

Requirements
- Python 3
- NumPy
in bash 'pip install numpy'


Limitations
- Small dataset — predictions won't be highly accurate
- Only supports 4 niches and a fixed set of countries (see countryCPM.py)
- Simple linear model — doesn't capture more complex real-world factors 
- Model retrains from scratch every time the script runs 

