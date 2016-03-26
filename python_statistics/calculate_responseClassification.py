from .calculate_dependencies import *
from .calculate_base import calculate_base
class calculate_responseClassification(calculate_base):
    def extract_responseClassification(self,data_model_I=None,
        response_method_I=None,
        response_options_I=None,
        raise_I=False):
        '''
        INPUT:
        data_model_I = classification or regression model

        covariance models:
        mahalanobis

        trees:
        predict_log_proba
        predict_proba

        svm:
        decision_function

        nearest neighbors:
        kneighbors
        kneighbors_graph
        radius_neighbors
        radius_neighbors_graph 

        clustering:
        predict

        '''
        if data_model_I: data_model=data_model_I;
        else: data_model = self.data_model;
        responses_O = None;
        try:
            if hasattr(data_model, response_method_I):
                responses_O = data_model.response_method_I();
        except Exception as e:
            if raise_I: raise;
            else: print(e);
        return responses_O;

    def extract_classProbabilities(self,data_model_I=None,
        response_method_I=None,
        response_options_I=None,
        raise_I=False):
        '''
        INPUT:
        data_model_I = tree, 

        '''
        if data_model_I: data_model=data_model_I;
        else: data_model = self.data_model;
        response_values_O,response_labels_O = None,None;
        try:
            if hasattr(data_model, 'predict_proba'):
                response_values_O = data_model.predict_proba(self.data_train['data']);
                response_labels_O = pd.Series(self.data_train['response']).unique();
        except Exception as e:
            if raise_I: raise;
            else: print(e);
        return response_values_O,response_labels_O;

    def extract_decisionFunction(self,data_model_I=None,
        response_method_I=None,
        response_options_I=None,
        raise_I=False):
        '''
        INPUT:
        data_model_I = svm, 
        decision_function_shape='ovr'

        '''
        if data_model_I: data_model=data_model_I;
        else: data_model = self.data_model;
        response_values_O,response_labels_O = None,None;
        try:
            if hasattr(data_model, 'decision_function'):
                responses_O = data_model.decision_function(self.data_train['data']);

        except Exception as e:
            if raise_I: raise;
            else: print(e);
        return response_values_O,response_labels_O;