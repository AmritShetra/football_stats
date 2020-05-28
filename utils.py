import matplotlib.pyplot as plt

def capitalise(string):
    '''
    Capitalises string and replaces underscores with spaces.
    '''
    if len(string.split('_')) == 1:
        return string.capitalize()
    else:
        return " ".join(word.capitalize() for word in string.split('_')[:-1]) + \
               " " + string.split('_')[-1].capitalize()

def plot_scatter(dataset, key_name, target):
    '''
    Creates scatter graph comparing a target (e.g. fpl_value) and a feature of the dataset.
    '''
    plt.scatter(
        dataset[key_name], dataset[target]
    )
    key_name = capitalise(key_name)
    target = capitalise(target)
    plt.title(key_name + " vs " + target)
    plt.xlabel(key_name)
    plt.ylabel(target)
    plt.show()

