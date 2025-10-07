from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def uniform(self):
        pass
    @abstractmethod
    def payTT(self):
        pass
class QA(Employee):
    def uniform(self):
        print("you can wear anything you want")
        
    
newQA =QA()
newQA.uniform()