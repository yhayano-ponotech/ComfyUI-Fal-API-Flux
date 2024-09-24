class FalAPIFluxControlNetConfigNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("STRING", {
                    "multiline": False,
                    "default": "lllyasviel/sd-controlnet-canny"
                }),
                "control_image": ("IMAGE",),
                "conditioning_scale": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.1,
                    "max": 2.0,
                    "step": 0.1
                }),
            },
            "optional": {
                "config_url": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "variant": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
            }
        }

    RETURN_TYPES = ("CONTROLNET_CONFIG",)
    FUNCTION = "configure_controlnet"
    CATEGORY = "image generation"

    def configure_controlnet(self, path, control_image, conditioning_scale, config_url="", variant=""):
        return ({
            "path": path,
            "control_image": control_image,
            "conditioning_scale": conditioning_scale,
            "config_url": config_url if config_url else None,
            "variant": variant if variant else None
        },)

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxControlNetConfigNode": FalAPIFluxControlNetConfigNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxControlNetConfigNode": "Fal API Flux ControlNet Config"
}