import numpy as np
from sklearn.metrics import precision_score, recall_score

class PrecisionRecallCalculator:
    def __init__(self, n):
        self.n = n
        self.data = np.zeros((n, 2), dtype=int)

    def inputData(self):
        for i in range(self.n):
            x = int(input(f"Please enter x value (ground truth class) for point {i+1}: "))
            y = int(input(f"Please enter y value (predicted class) for point {i+1}: "))
            self.data[i] = [x, y]
    
    def calculatePrecisionRecall(self):
        x = self.data[:, 0]  # Ground truth labels
        y = self.data[:, 1]  # Predicted labels
        
        precision = precision_score(x, y, zero_division=0)
        recall = recall_score(x, y, zero_division=0)
        
        return precision, recall

def main():
    # Input the number of points N
    n = int(input("Please enter the number of points (N): "))
    
    # Create an instance of the PrecisionRecallCalculator
    calculator = PrecisionRecallCalculator(n)
    
    # Input the data
    calculator.inputData()
    
    # Calculate and display the precision and recall
    precision, recall = calculator.calculatePrecisionRecall()
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")

if __name__ == "__main__":
    main()