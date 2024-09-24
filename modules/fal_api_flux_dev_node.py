from .base_fal_api_flux_node import BaseFalAPIFluxNode

class FalAPIFluxDevNode(BaseFalAPIFluxNode):
    def __init__(self):
        super().__init__()
        self.set_api_endpoint("fal-ai/flux/dev")
        
    @classmethod
    def INPUT_TYPES(cls):
        return super().INPUT_TYPES()

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxDevNode": FalAPIFluxDevNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxDevNode": "Fal API Flux Dev"
}