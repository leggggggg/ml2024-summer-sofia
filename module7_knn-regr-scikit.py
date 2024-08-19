import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.exceptions import NotFittedError

class KNNRegressionModel:
    def __init__(self, n):
        self.n = n
        self.xTrain = np.zeros((n, 1))  
        self.yTrain = np.zeros(n) 
        self.k = None
        self.model = None

    def inputData(self):
        self.k = int(input("Please enter a positive integer k (number of neighbors): "))
        
        # Ensure k is valid
        if self.k > self.n:
            print("Error: k cannot be larger than N.")
            exit()
        
        # Collect the N points
        for i in range(self.n):
            x = float(input(f"Enter x value for point {i + 1}: "))
            y = float(input(f"Enter y value for point {i + 1}: "))
            self.xTrain[i] = x
            self.yTrain[i] = y
    
    def fitModel(self):
        try:
            self.model = KNeighborsRegressor(n_neighbors=self.k)
            self.model.fit(self.xTrain, self.yTrain)
        except NotFittedError:
            print("Error: The model could not be fitted. Please check your inputs.")
            exit()
    
    def predict(self, xTest):
        if self.model is None:
            print("Error: The model is not trained.")
            return
        
        yPred = self.model.predict([[xTest]])  # Make prediction
        return yPred[0]
    
    def calculateVariance(self):
        return np.var(self.yTrain)

def main():
    # Input the number of points N
    n = int(input("Please enter a positive integer N (number of points): "))
    
    # Create an instance of the KNNRegressionModel
    knnModel = KNNRegressionModel(n)
    
    # Input the data and train the model
    knnModel.inputData()
    knnModel.fitModel()
    
    # Input the X value for prediction
    xTest = float(input("Enter X value for prediction: "))
    
    # Predict the y value and display the result
    yPred = knnModel.predict(xTest)
    print(f"Predicted Y value for X = {xTest} is: {yPred}")
    
    # Calculate and display the variance of the labels
    variance = knnModel.calculateVariance()
    print(f"The variance of the labels (y values) is: {variance}")

if __name__ == "__main__":
    main()