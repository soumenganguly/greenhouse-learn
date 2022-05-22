from joblib import load
import pkg_resources

MODEL = pkg_resources.resource_filename('ghlearn', 'model_storage/GREENHOUSE_PREDICTION.model')

class GreenHousePredictor:
    def __init__(self):
        self.model = load(MODEL)

    def train(self, X_train, Y_train):
        X_train = X_train.drop('time', axis=1)
        Y_train = Y_train.drop('time', axis=1)
        
        self.model.fit(X_train, Y_train)
        return self

    def predict(self, X_test):
        if 'time' in X_test.columns:
            X_test = X_test.drop('time', axis=1)
        
        y_pred = self.model.predict(X_test)
        return y_pred