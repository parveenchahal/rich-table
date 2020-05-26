from abc import abstractmethod
class DbOperations(object):
    
    @abstractmethod
    def execute_query(self, query):
        raise NotImplementedError()