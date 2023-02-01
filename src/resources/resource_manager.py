class ResourceManager:
    def __init__(self):
        self.resources = {
            'scanner': 1,
            'printer': 2,
            'modem': 1,
            'sata': 2
        }
        self.allocated_resources = {
            'scanner': 0,
            'printer': 0,
            'modem': 0,
            'sata': 0
        }
        pass

    def __can_alloc(self, process):
        for resource, max_quantity in self.resources.items():
            proc_quantity = getattr(process, resource)

            if(proc_quantity > max_quantity):
                print(f'O Processo {process.pid} não conseguiu ser criado (recursos insuficientes).')
                return False

            if(proc_quantity > max_quantity-self.allocated_resources[resource]):
                print(f"O processo {process.pid} foi bloqueado (não conseguiu obter {resource} - requisitado: {proc_quantity} (disponível {max_quantity-self.allocated_resources[resource]})).")
                return False
            
        return True

    def request(self, process):
        if(not self.__can_alloc()):
            return False

        for resource in self.resources:
            proc_quantity = getattr(process, resource)
            self.allocated_resources[resource] = proc_quantity
            
    def deallocate(self, process):
        for resource in self.resources:
            proc_quantity = getattr(process, resource)
            self.allocated_resources[resource] -= proc_quantity
