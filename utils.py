import matplotlib.pyplot as plt

def capitalise(string):
    '''
    Capitalises string and replaces underscores with spaces.
    '''
    if len(string.split('_')) == 1:
        return string.capitalize()
    else:
        " ".join(word.capitalize() for word in string.split('_')[:-1]) + \
            " " + string.split('_')[-1].capitalize()

def plot_scatter(dataset, key_name):
    '''
    Creates scatter graph comparing market value and a feature of the dataset.
    '''
    plt.scatter(
        dataset[key_name], dataset['market_value']
    )
    key_name = capitalise(key_name)
    plt.title(key_name + " vs Market Value")
    plt.xlabel(key_name)
    plt.ylabel('Market Value')
    plt.show()

