class FalAPIFluxControlNetUnionConfigNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("STRING", {
                    "multiline": False,
                    "default": "https://huggingface.co/InstantX/FLUX.1-dev-Controlnet-Union/resolve/main/diffusion_pytorch_model.safetensors"
                }),
                "control_image": ("IMAGE",),
                "control_mode": (["canny", "tile", "depth", "blur", "pose", "gray", "lq"],),
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

    RETURN_TYPES = ("CONTROLNET_UNION_CONFIG",)
    FUNCTION = "configure_controlnet_union"
    CATEGORY = "image generation"

    def configure_controlnet_union(self, path, control_image, control_mode, conditioning_scale, config_url="", variant=""):
        return ({
            "path": path,
            "controls": [{
                "control_image_url": control_image,
                "control_mode": control_mode,
                "conditioning_scale": conditioning_scale
            }],
            "config_url": config_url if config_url else None,
            "variant": variant if variant else None
        },)

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxControlNetUnionConfigNode": FalAPIFluxControlNetUnionConfigNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxControlNetUnionConfigNode": "Fal API Flux ControlNet Union Config"
}