from utils.singleton import Singleton
from utils.output import *


class ResourceManager(metaclass=Singleton):
    def __init__(self):
        self.out = Output()
        self.resources = {
            'printer': 2,
            'scanner': 1,
            'modem': 1,
            'sata': 2
        }
        self.allocated_resources = {
            'printer': 0,
            'scanner': 0,
            'modem': 0,
            'sata': 0
        }
        self.resource_process = {
            'printer': [],
            'scanner': [],
            'modem': [],
            'sata': []
        }

    def __can_alloc(self, process):
        for resource, max_quantity in self.resources.items():
            proc_quantity = getattr(process, resource)

            if(proc_quantity > max_quantity):
                self.out.error(EXCEEDED_RESOURCES, pid=process.pid)
                return -1

            if(proc_quantity > max_quantity-self.allocated_resources[resource]):
                if(process.pid in self.resource_process[resource]):
                    return 1
                self.out.error(BLOCKED_DUE_RESOURCES, pid=process.pid, resource=resource, proc_quantity=proc_quantity, max_quantity=max_quantity, remaning=self.allocated_resources[resource])
                return 0
            
        return 1

    def request(self, process):
        result = self.__can_alloc(process)
        if(result <= 0):
            return result
        
        for resource in self.resources:
            if(process.pid in self.resource_process[resource]):
                return 1
            proc_quantity = getattr(process, resource)
            self.allocated_resources[resource] += proc_quantity
            self.resource_process[resource].append(process.pid)
        
        return 1
            
    def deallocate(self, process):
        for resource in self.resources:
            proc_quantity = getattr(process, resource)
            self.allocated_resources[resource] -= proc_quantity
            self.resource_process[resource].remove(process.pid)
