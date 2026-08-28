import numpy as np
from countryCPM import get_country_level


def load_data(filename):
    data = np.genfromtxt(filename, delimiter=',', skip_header=1)
    X = data[:,:-1]
    y = data[:,-1]


    X[:,2] = X[:,2] / 100


    mu = np.mean(X, axis = 0)
    sigma = np.std(X, axis = 0)


    X_norm = (X - mu) / sigma


    return X_norm , y, mu, sigma

def compute_modelOutput(X, w, b):
    f_wb = np.dot(X, w) + b
    return f_wb

def compute_Cost(X, y , w , b):
    f_wb = np.dot(X, w) + b

    m = X.shape[0]
    sum_cost = 0
    for i in range(m):
        cost = (f_wb[i] - y[i])**2
        sum_cost += cost

    sum_cost = sum_cost / (2*m)

    return sum_cost

def compute_Gradient(X, y, w, b):
    f_wb = np.dot(X, w) + b

    m,n = X.shape
    dw = np.zeros(n)
    db = 0.0

    
    for i in range(m):
        error = f_wb[i] - y[i]
        dw += error * X[i]
        db += error

    dw /= m
    db /= m


    return dw, db

def gradeint_Descent(X, y , w_init, b_init, alpha, iters):
    w = w_init
    b = b_init

    

    for i in range(iters):
        dw, db = compute_Gradient(X, y, w, b)
        w = w - alpha*dw
        b = b - alpha*db


    return w, b


X_train, y_train, mu, sigma = load_data("youtube_data.txt")

w_init = np.zeros(X_train.shape[1])
b_init = 0.0

alpha = 0.01
iters = 10000

valid_niches = {"tech": 0, "gaming": 1, "finance": 2, "education": 3}

while True:
    niche_selected = input("# Enter your niche [tech / gaming / finance / education]: ").strip().lower()
    
    if niche_selected not in valid_niches:
        print("Please choose from the above categories.\n")
    else:
        niche = valid_niches[niche_selected]
        break

while True:
    country = input("- Enter the country: ").strip().lower()
    if get_country_level(country) is None:
        print("Please enter correct country.\n")
    else:
        break
        
while True:
    try:
        duration = float(input("- Enter vid duration(min): "))
        break
    except:
        print("Enter numbers ONLY\n")

while True:
    try:
        retention = float(input("- Enter retention %: "))
        break
    except:
        print("Enter numbers ONLY\n")

retention = retention / 100
print("")
w_final, b_final = gradeint_Descent(X_train, np.log(y_train), w_init, b_init, alpha, iters )

c = get_country_level(country)


X_new = np.array([c, duration, retention, niche])
X_new_norm = (X_new - mu) / sigma 

prediction = compute_modelOutput(X_new_norm, w_final, b_final)
prediction = np.exp(prediction)

prediction = max(float(prediction), 0.0)
print("\n------------------------------------------")
print(f"Your profit is {float(prediction):.2f} $ per 1000 views.")
print("------------------------------------------")

