import torch
import numpy as np
import pandas as pd

def load_data():
    
    try:
        
        #_x_train = pd.read_csv(r"C:\Users\91939\Downloads\datasets\Linear_X_Train.csv").astype(np.float32)
        #_y_train = pd.read_csv(r"C:\Users\91939\Downloads\datasets\Linear_Y_Train.csv").astype(np.float32)

        #_x_train = torch.tensor(_x_train.values)
        #_y_train = torch.tensor(_y_train.values)
        
        _x_train = np.array([[3.3], [4.4], [5.5], [6.71], [6.93], [4.168], [9.779], [6.182], [7.59], [2.167], [7.042], [10.791], [5.313], [7.997], [3.1]], dtype=np.float32)
        _y_train = np.array([[1.7], [2.76], [2.09], [3.19], [1.694], [1.573], [3.366], [2.596], [2.53], [1.221], [2.827], [3.465], [1.65], [2.904], [1.3]], dtype=np.float32)
        
        _x_train = torch.from_numpy(_x_train)
        _y_train = torch.from_numpy(_y_train)
        
        return _x_train, _y_train
        
    except FileNotFoundError as error:
        print("File Not Found Error during loading data")
        raise error

    except Exception as error:
        print("Exception Error: load_data")
        print(error)
        raise error