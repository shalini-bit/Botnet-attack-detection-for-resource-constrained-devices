import pandas as pd
import os
from glob import glob
    
def load_device_data_multi_label(PATH, EXT, device):
    """
    Creates a data frame consisting of individual device data. 
    The directory should be where the unzipped data files are stored. 
    Assumes the file structurce is
        device name
            mirai_attacks(folder)
            gafgyt_attacks(folder)
            benign_traffic.csv
    Parameters
    ----------
    PATH : str
        The directory in which the data files are stored. 
    EXT : str
        Extension of the file
    device : str
        Device Name
        
    Returns
    -------
    device_data : pandas data frame consisting of specific device 
                  data with 11 different classes.
    """
    try:
        dfs = []
        for path, subdir, files in os.walk(PATH):
            for file in glob(os.path.join(path, EXT)):
                if file.split('\\')[1] == device:
                    data = pd.read_csv(file)
                    label = file.split('\\')
                    if len(label) == 3:
                        data['label'] = label[2].split('_')[0]
                    else:
                        data['label'] = label[2].split('_')[0] + '_' + label[3].split('.')[0]
                    data['device'] = file.split('\\')[1]
                    dfs.append(data)
                        
        device_data = pd.concat(dfs, ignore_index=True)
        
        return device_data
        
    except Exception as e:
        return str(e)


def load_all_data(PATH, EXT):
    """
    Creates a data frame consisting of all the device data. 
    The directory should be where the unzipped data files are stored. 
    Assumes the file structurce is
        device name
            mirai_attacks(folder)
            gafgyt_attacks(folder)
            benign_traffic.csv
    Parameters
    ----------
    PATH : str
        The directory in which the data files are stored. 
    EXT : str
        Extension of the file
        
    Returns
    -------
    device_data : pandas data frame contain all the device data with 11 classes
                which is device specified.
    """
    try:
        dfs = []
        for path, subdir, files in os.walk(PATH):
            for file in glob(os.path.join(path, EXT)):
                data = pd.read_csv(file)
                label = file.split('\\')
                if len(label) == 3:
                    data['label'] = label[1] + '_' + label[2].split('_')[0]
                else:
                    data['label'] = label[1] + '_' + label[2].split('_')[0] + '_' + label[3].split('.')[0]
                
                data['device'] = file.split('\\')[1]
                dfs.append(data)
        device_data = pd.concat(dfs, ignore_index = True)
        
        return device_data
    except Exception as e:
        return str(e)


def load_all_data_class(PATH, EXT):
    """
    Creates a data frame consisting of all the device data. 
    The directory should be where the unzipped data files are stored. 
    Assumes the file structurce is
        device name
            mirai_attacks(folder)
            gafgyt_attacks(folder)
            benign_traffic.csv
    Parameters
    ----------
    PATH : str
        The directory in which the data files are stored. 
    EXT : str
        Extension of the file
        
    Returns
    -------
    device_data : pandas data frame contain all the device data with 3 classes
                which is Not device specified.
    """
    try:
        dfs = []
        for path, subdir, files in os.walk(PATH):
            for file in glob(os.path.join(path, EXT)):
                data = pd.read_csv(file)
                label = file.split("\\")
                if len(label) == 3:
                    data['label'] = label[2].split('_')[0]
                else:
                    data['label'] = label[2].split('_')[0]
                data['device'] = file.split('\\')[1]
                sampled_data = data.sample(frac=0.15)
                dfs.append(sampled_data)
        device_data = pd.concat(dfs, ignore_index = True)
        return device_data
    
    except Exception as e:
        return(str(e))

    
def load_all_data_multi_class(PATH, EXT):
    """
    Creates a data frame consisting of all the device data. 
    The directory should be where the unzipped data files are stored. 
    Assumes the file structurce is
        device name
            mirai_attacks(folder)
            gafgyt_attacks(folder)
            benign_traffic.csv
    Parameters
    ----------
    PATH : str
        The directory in which the data files are stored. 
    EXT : str
        Extension of the file
        
    Returns
    -------
    device_data : pandas data frame contain all the device data with 11 classes
                which is Not device specified.
    """
    try:
        dfs = []
        for path, subdir, files in os.walk(PATH):
            for file in glob(os.path.join(path, EXT)):
                data = pd.read_csv(file)
                label = file.split('\\')
                if len(label) == 3:
                    data['label'] = label[2].split('_')[0]
                else:
                    data['label'] = label[2].split('_')[0] + '_' + label[3].split('.')[0]
                
                data['device'] = file.split('\\')[1]
                sampled_data = data.sample(frac=0.15)
                dfs.append(sampled_data)
        device_data = pd.concat(dfs, ignore_index = True)
        
        return device_data
    except Exception as e:
        return str(e)