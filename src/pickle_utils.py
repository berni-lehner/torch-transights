import pickle

def save_data(data, filename):
    """
    Save data to a binary file using pickle serialization.

    Parameters:
    data (Any): The data to be saved.
    filename (str): The name of the file to save the data to.

    Returns:
    None
    """
    with open(filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)

def load_data(filename):
    """
    Load data from a binary file using pickle deserialization.

    Parameters:
    filename (str): The name of the file to load data from.

    Returns:
    Any: The loaded data.
    """
    with open(filename, 'rb') as pickle_file:
        data = pickle.load(pickle_file)

    return data
