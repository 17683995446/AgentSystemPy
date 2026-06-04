from ..interfaces.i_resource_cost_model import IResourceCostModel


class ResourceCostModelImpl(IResourceCostModel):
    def estimate_cpu(self, path: dict) -> float:
        return 0.0

    def estimate_mem(self, path: dict) -> float:
        return 0.0

    def estimate_io(self, path: dict) -> float:
        return 0.0
