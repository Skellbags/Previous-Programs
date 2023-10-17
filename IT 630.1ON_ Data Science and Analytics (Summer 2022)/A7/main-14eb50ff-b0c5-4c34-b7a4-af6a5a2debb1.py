"""
Ryan J. Skelly - rjs1070 - Prof. Narayan
A7 - 6/24/22 - Purpose:
    Plotting various Graphs based on file input
Note:
    All of my values were slightly off of the sample output, although I 
    couldn't pinpoint a reason why(I'm guessing some sort of variation between
    input files). $fs and $ext for file(s) and extention
    
Supported Files:
    in1.txt
    in2.txt
    in3.txt
    in4.txt
"""
fs=["in1", "in2", "in3", "in4"]
ext=".txt"

import pandas as pd
import regression_functions as regress
import matplotlib.pyplot as plt
    
def endit(n,o):
    axs[n,o].grid(color='0.8', linestyle='-', linewidth=2)
    axs[n,o].scatter(x, y, color='red', label="Data Value")
    axs[n,o].plot(x, fx, 'b', label="Best Fit")
    axs[n,o].set_title('Data From: '+fs[ind], fontweight='bold')
    axs[n,o].set_title("Pearson Correlation Coefficient: %12.6f" % pearson_r+"\n"+"Coefficient of determination: %12.6f" % coeff_of_determination, loc="left")
    axs[n,o].set_xlabel('x-axis', fontweight='bold')
    axs[n,o].set_ylabel('y-axis', fontweight='bold')
    if(ind==2):
        axs[n,o].legend(loc="upper left")
    else:
        axs[n,o].legend()
        
if __name__ == "__main__":
    print("#### RJS1070 - IT 630 - A7 - 6/24/22 ####")
    print("############### Plott-in ################\n")
    
    fig, axs = plt.subplots(2, 2, figsize=(20,12), sharey=False)
    for ind in range(len(fs)):
        data = pd.read_csv(fs[ind]+ext)
        x=[]
        y=[]
        for i in data.values:
            x.append(i.tolist()[0])
            y.append(i.tolist()[1])
        m, b = regress.compute_m_and_b(x, y)
        fx, residual = regress.compute_fx_residual(x, y, m, b)
        least_squares_r = regress.compute_sum_of_squared_residuals(residual)
        sum_squares = regress.compute_total_sum_of_squares(y)
        print("\n#########################################")
        print("Input File:  ", ind)
        print("Data points: ", len(x))
        print("Least Squares Method")
        print("####################")
        print("Coefficients: m =", "%8.6f" % m, "\tb =", "%8.6f" % b)
        print("Sum of Squared Residuals: %12.6f" % least_squares_r)
        print("Total Sum of Squares: %12.6f" % sum_squares)
        coeff_of_determination = (1 - (least_squares_r/sum_squares))
        print("Coefficient of determination: %12.6f" % coeff_of_determination)
        print()
        pearson_r = regress.compute_pearson_coefficient(x, y)
        print("Pearson Method")
        print("##############")
        print("Pearson Correlation Coefficient: %12.6f" % pearson_r)
        print("#########################################")
        if ind==0:
            endit(0,0)
        elif ind==1:
            endit(0,1)
        elif ind==2:
            endit(1,0)
        else:
            endit(1,1)
    fig.tight_layout()