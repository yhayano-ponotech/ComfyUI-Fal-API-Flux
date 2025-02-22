from .modules.fal_api_flux_dev_node import FalAPIFluxDevNode
from .modules.fal_api_flux_dev_image_to_image_node import FalAPIFluxDevImageToImageNode
from .modules.fal_api_flux_dev_with_lora_node import FalAPIFluxDevWithLoraNode
from .modules.fal_api_flux_dev_with_lora_image_to_image_node import FalAPIFluxDevWithLoraImageToImageNode
from .modules.fal_api_flux_dev_with_lora_inpaint_node import FalAPIFluxDevWithLoraInpaintNode
from .modules.fal_api_flux_dev_with_lora_and_controlnet_node import FalAPIFluxDevWithLoraAndControlNetNode
from .modules.fal_api_flux_dev_with_lora_and_controlnet_image_to_image_node import FalAPIFluxDevWithLoraAndControlNetImageToImageNode
from .modules.fal_api_flux_dev_with_lora_and_controlnet_inpaint_node import FalAPIFluxDevWithLoraAndControlNetInpaintNode
from .modules.fal_api_flux_pro_node import FalAPIFluxProNode
from .modules.fal_api_flux_pro_v11_node import FalAPIFluxProV11Node
from .modules.fal_api_flux_pro_v11_ultra_node import FalAPIFluxProV11UltraNode
from .modules.fal_api_flux_lora_config_node import FalAPIFluxLoraConfigNode
from .modules.fal_api_flux_controlnet_config_node import FalAPIFluxControlNetConfigNode
from .modules.fal_api_flux_controlnet_union_config_node import FalAPIFluxControlNetUnionConfigNode
from .modules.fal_api_flux_pro_canny_node import FalAPIFluxProCannyNode
from .modules.fal_api_flux_pro_depth_node import FalAPIFluxProDepthNode
from .modules.fal_api_flux_pro_fill_node import FalAPIFluxProFillNode
from .modules.fal_api_flux_pro_redux_node import FalAPIFluxProReduxNode
from .modules.fal_api_flux_dev_canny_with_lora_node import FalAPIFluxDevCannyWithLoraNode

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
    "FalAPIFluxProV11Node": FalAPIFluxProV11Node,
    "FalAPIFluxProV11UltraNode": FalAPIFluxProV11UltraNode,
    "FalAPIFluxLoraConfigNode": FalAPIFluxLoraConfigNode,
    "FalAPIFluxControlNetConfigNode": FalAPIFluxControlNetConfigNode,
    "FalAPIFluxControlNetUnionConfigNode": FalAPIFluxControlNetUnionConfigNode,
    "FalAPIFluxProCannyNode": FalAPIFluxProCannyNode,
    "FalAPIFluxProDepthNode": FalAPIFluxProDepthNode,
    "FalAPIFluxProFillNode": FalAPIFluxProFillNode,
    "FalAPIFluxProReduxNode": FalAPIFluxProReduxNode,
    "FalAPIFluxDevCannyWithLoraNode": FalAPIFluxDevCannyWithLoraNode
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
    "FalAPIFluxProV11Node": "Fal API Flux Pro V1.1",
    "FalAPIFluxProV11UltraNode": "Fal API Flux Pro v1.1 Ultra",
    "FalAPIFluxLoraConfigNode": "Fal API Flux LoRA Config",
    "FalAPIFluxControlNetConfigNode": "Fal API Flux ControlNet Config",
    "FalAPIFluxControlNetUnionConfigNode": "Fal API Flux ControlNet Union Config",
    "FalAPIFluxDevImageToImageNode": "Fal API Flux Dev Image-to-Image",
    "FalAPIFluxProCannyNode": "Fal API Flux Pro Canny",
    "FalAPIFluxProDepthNode": "Fal API Flux Pro Depth",
    "FalAPIFluxProFillNode": "Fal API Flux Pro Fill",
    "FalAPIFluxProReduxNode": "Fal API Flux Pro Redux",
    "FalAPIFluxDevCannyWithLoraNode": "Fal API Flux Dev Canny With LoRA"
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
    'FalAPIFluxProV11Node',
    "FalAPIFluxProV11UltraNode",
    'FalAPIFluxLoraConfigNode', 
    'FalAPIFluxControlNetConfigNode', 
    'FalAPIFluxControlNetUnionConfigNode',
    'FalAPIFluxProCannyNode',
    'FalAPIFluxProDepthNode',
    'FalAPIFluxProFillNode',
    'FalAPIFluxProReduxNode',
    'FalAPIFluxDevCannyWithLoraNode'
]