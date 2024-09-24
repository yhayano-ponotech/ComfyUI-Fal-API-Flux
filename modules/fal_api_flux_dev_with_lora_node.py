from .base_fal_api_flux_node import BaseFalAPIFluxNode

class FalAPIFluxDevWithLoraNode(BaseFalAPIFluxNode):
    def __init__(self):
        super().__init__()
        self.set_api_endpoint("fal-ai/flux-lora")
        
    def set_api_endpoint(self, endpoint):
        super().set_api_endpoint(endpoint)
        
    @classmethod
    def INPUT_TYPES(cls):
        input_types = super().INPUT_TYPES()
        input_types["optional"].update({
            "lora": ("LORA_CONFIG",),
        })
        return input_types
    

    def prepare_arguments(self, lora=None, **kwargs):
        arguments = super().prepare_arguments(**kwargs)
        
        if lora:
            arguments["loras"] = [lora]

        return arguments

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxDevWithLoraNode": FalAPIFluxDevWithLoraNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxDevWithLoraNode": "Fal API Flux Dev With LoRA"
}