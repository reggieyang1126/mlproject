import pickle
import sys
from src.exception import CustomException
import os

def save_object(file_path,obj):
    """
    Save the object to the specified file path
    """
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path, "wb") as f:
            pickle.dump(obj, f)
            
    except Exception as e:
        raise CustomException(e,sys)