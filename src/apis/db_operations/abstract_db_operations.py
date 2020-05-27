from abc import abstractmethod
class DbOperations(object):
    
    @abstractmethod
    def query_all(self, model, schema):
        raise NotImplementedError()