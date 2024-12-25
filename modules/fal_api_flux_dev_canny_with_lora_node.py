import logging

from .base_fal_api_flux_node import BaseFalAPIFluxNode

logger = logging.getLogger(__name__)


class FalAPIFluxDevCannyWithLoraNode(BaseFalAPIFluxNode):
    def __init__(self):
        super().__init__()
        self.set_api_endpoint("fal-ai/flux-lora-canny")

    def set_api_endpoint(self, endpoint):
        super().set_api_endpoint(endpoint)

    @classmethod
    def INPUT_TYPES(cls):
        input_types = super().INPUT_TYPES()
        # Add control image input
        input_types["required"].update({
            "control_image": ("IMAGE",),  # Accept input from another node
        })
        input_types["optional"].update({
            "lora_1": ("LORA_CONFIG",),
            "lora_2": ("LORA_CONFIG",),
            "lora_3": ("LORA_CONFIG",),
            "lora_4": ("LORA_CONFIG",),
            "lora_5": ("LORA_CONFIG",),
        })

        return input_types

    def prepare_arguments(self, control_image, lora_1=None, lora_2=None, lora_3=None, lora_4=None, lora_5=None,
                          **kwargs):
        # Get base arguments from parent class
        arguments = super().prepare_arguments(**kwargs)

        # Upload the control image and get its URL
        control_image_url = self.upload_image(control_image)
        logger.info(f"Uploaded control image. URL: {control_image_url}")

        # Update arguments with Canny-specific parameters
        arguments.update({
            "image_url": control_image_url
        })

        # Collect all provided LoRA configurations
        loras = []
        for lora in [lora_1, lora_2, lora_3, lora_4, lora_5]:
            if lora is not None:
                loras.append(lora)

        if loras:
            arguments["loras"] = loras

        return arguments


NODE_CLASS_MAPPINGS = {
    "FalAPIFluxDevCannyWithLoraNode": FalAPIFluxDevCannyWithLoraNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxDevCannyWithLoraNode": "Fal API Flux Dev Canny With LoRA"
}
