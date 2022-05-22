def train_test_split(data, train_size, predict_on='Tair'):
    '''
    Parameters
    -----------
    data: dataframe
    train_size: ratio of training data
    predict_on: Set the dependent variable (Tair/Rhair)
    '''
    data.reset_index(inplace=True)
    # handled in train and predict
    # data.drop('time', axis=1, inplace=True)
    
    train_set = data[:int(len(data)*train_size)]
    test_set = data[int(len(data)*train_size):]
    
    train_columns = data.columns.drop(['Tair', 'Rhair'])
    
    X_train, Y_train = train_set[train_columns], train_set[predict_on]
    X_test, Y_test = test_set[train_columns], test_set[predict_on]
    
    return X_train, Y_train, X_test, Y_test