import numpy as np

class KNNRegression:
    def __init__(self, k, points):
        self.k = k
        self.points = np.array(points)

    def predict(self, X):
        # Calculate distances between X and all x of the points
        distances = np.abs(self.points[:, 0] - X)
        
        # Get the index of the k smallest distances
        nearestIndex = np.argsort(distances)[:self.k]
        
        # Get the y values of the nearest points
        nearestY = self.points[nearestIndex, 1]
        
        # Return the mean of the nearest y values
        return np.mean(nearestY)

def main():
    N = int(input("Please enter the number of points (N): "))
    k = int(input("Please enter the number of neighbors (k): "))

    if k > N:
        print("Error: k cannot be greater than N")
        return

    points = []
    for i in range(N):
        x = float(input(f"Please enter x value for point {i+1}: "))
        y = float(input(f"Please enter y value for point {i+1}: "))
        points.append((x, y))
    
    knn = KNNRegression(k, points)

    X = float(input("Please enter the X value for which you want to predict Y: "))
    predictedY = knn.predict(X)
    
    print(f"The predicted Y value is: {predictedY}")

if __name__ == "__main__":
    main()