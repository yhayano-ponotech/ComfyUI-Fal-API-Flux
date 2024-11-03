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
            "lora_1": ("LORA_CONFIG",),
            "lora_2": ("LORA_CONFIG",),
            "lora_3": ("LORA_CONFIG",),
            "lora_4": ("LORA_CONFIG",),
            "lora_5": ("LORA_CONFIG",),
        })
        return input_types

    def prepare_arguments(self, lora_1=None, lora_2=None, lora_3=None, lora_4=None, lora_5=None, **kwargs):
        arguments = super().prepare_arguments(**kwargs)
        
        # Collect all provided LoRA configurations
        loras = []
        for lora in [lora_1, lora_2, lora_3, lora_4, lora_5]:
            if lora is not None:
                loras.append(lora)
        
        if loras:
            arguments["loras"] = loras

        return arguments

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxDevWithLoraNode": FalAPIFluxDevWithLoraNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxDevWithLoraNode": "Fal API Flux Dev With LoRA"
}