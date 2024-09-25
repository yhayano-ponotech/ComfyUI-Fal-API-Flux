from .modules.fal_api_flux_dev_node import FalAPIFluxDevNode
from .modules.fal_api_flux_dev_image_to_image_node import FalAPIFluxDevImageToImageNode
from .modules.fal_api_flux_dev_with_lora_node import FalAPIFluxDevWithLoraNode
from .modules.fal_api_flux_dev_with_lora_image_to_image_node import FalAPIFluxDevWithLoraImageToImageNode
from .modules.fal_api_flux_dev_with_lora_inpaint_node import FalAPIFluxDevWithLoraInpaintNode
from .modules.fal_api_flux_dev_with_lora_and_controlnet_node import FalAPIFluxDevWithLoraAndControlNetNode
from .modules.fal_api_flux_dev_with_lora_and_controlnet_image_to_image_node import FalAPIFluxDevWithLoraAndControlNetImageToImageNode
from .modules.fal_api_flux_dev_with_lora_and_controlnet_inpaint_node import FalAPIFluxDevWithLoraAndControlNetInpaintNode
from .modules.fal_api_flux_pro_node import FalAPIFluxProNode
from .modules.fal_api_flux_lora_config_node import FalAPIFluxLoraConfigNode
from .modules.fal_api_flux_controlnet_config_node import FalAPIFluxControlNetConfigNode
from .modules.fal_api_flux_controlnet_union_config_node import FalAPIFluxControlNetUnionConfigNode

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxDevNode": FalAPIFluxDevNode,
    "FalAPIFluxDevImageToImageNode": FalAPIFluxDevImageToImageNode,
    "FalAPIFluxDevWithLoraNode": FalAPIFluxDevWithLoraNode,
    "FalAPIFluxDevWithLoraImageToImageNode": FalAPIFluxDevWithLoraImageToImageNode,
    "FalAPIFluxDevWithLoraInpaintNode": FalAPIFluxDevWithLoraInpaintNode,
    "FalAPIFluxDevWithLoraAndControlNetNode": FalAPIFluxDevWithLoraAndControlNetNode,
    "FalAPIFluxDevWithLoraAndControlNetImageToImageNode": FalAPIFluxDevWithLoraAndControlNetImageToImageNode,
    "FalAPIFluxDevWithLoraAndControlNetInpaintNode": FalAPIFluxDevWithLoraAndControlNetInpaintNode,
    "FalAPIFluxProNode": FalAPIFluxProNode,
    "FalAPIFluxLoraConfigNode": FalAPIFluxLoraConfigNode,
    "FalAPIFluxControlNetConfigNode": FalAPIFluxControlNetConfigNode,
    "FalAPIFluxControlNetUnionConfigNode": FalAPIFluxControlNetUnionConfigNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxDevNode": "Fal API Flux Dev",
    "FalAPIFluxDevImageToImageNode": "Fal API Flux Dev Image-to-Image",
    "FalAPIFluxDevWithLoraNode": "Fal API Flux Dev with LoRA",
    "FalAPIFluxDevWithLoraImageToImageNode": "Fal API Flux Dev with LoRA Image-to-Image",
    "FalAPIFluxDevWithLoraInpaintNode": "Fal API Flux Dev with LoRA Inpaint",
    "FalAPIFluxDevWithLoraAndControlNetNode": "Fal API Flux with LoRA and ControlNet",
    "FalAPIFluxDevWithLoraAndControlNetImageToImageNode": "Fal API Flux with LoRA and ControlNet Image-to-Image",
    "FalAPIFluxDevWithLoraAndControlNetInpaintNode": "Fal API Flux with LoRA and ControlNet Inpaint",
    "FalAPIFluxProNode": "Fal API Flux Pro",
    "FalAPIFluxLoraConfigNode": "Fal API Flux LoRA Config",
    "FalAPIFluxControlNetConfigNode": "Fal API Flux ControlNet Config",
    "FalAPIFluxControlNetUnionConfigNode": "Fal API Flux ControlNet Union Config",
    "FalAPIFluxDevImageToImageNode": "Fal API Flux Dev Image-to-Image"
}

__all__ = [
    'FalAPIFluxDevNode', 
    'FalAPIFluxDevImageToImageNode', 
    'FalAPIFluxNodeWithControlNet', 
    'FalAPIFluxDevWithLoraImageToImageNode', 
    'FalAPIFluxDevWithLoraInpaintNode', 
    'FalAPIFluxDevWithLoraAndControlNetNode', 
    'FalAPIFluxDevWithLoraAndControlNetImageToImageNode', 
    'FalAPIFluxDevWithLoraAndControlNetInpaintNode',
    'FalAPIFluxProNode', 
    'FalAPIFluxLoraConfigNode', 
    'FalAPIFluxControlNetConfigNode', 
    'FalAPIFluxControlNetUnionConfigNode'
]