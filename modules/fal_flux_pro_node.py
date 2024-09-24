from .base_fal_api_flux_node import BaseFalAPIFluxNode
import fal_client
import logging

logger = logging.getLogger(__name__)

class FalAPIFluxProNode(BaseFalAPIFluxNode):
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True}),
                "image_size": (["square_hd", "square", "portrait_4_3", "portrait_16_9", "landscape_4_3", "landscape_16_9"],),
                "num_inference_steps": ("INT", {"default": 28, "min": 1, "max": 100}),
                "guidance_scale": ("FLOAT", {"default": 3.5, "min": 0.1, "max": 20.0}),
                "num_images": ("INT", {"default": 1, "min": 1, "max": 4}),
                "safety_tolerance": (["1", "2", "3", "4", "5", "6"],),
            },
            "optional": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "generate"
    CATEGORY = "image generation"

    def prepare_arguments(self, prompt, image_size, num_inference_steps, guidance_scale, num_images, safety_tolerance, seed=None):
        if not self.api_key:
            raise ValueError("API key is not set. Please check your config.ini file.")

        arguments = {
            "prompt": prompt,
            "image_size": image_size,
            "num_inference_steps": num_inference_steps,
            "guidance_scale": guidance_scale,
            "num_images": num_images,
            "safety_tolerance": safety_tolerance
        }

        if seed is not None and seed != 0:
            arguments["seed"] = seed

        return arguments

    def call_api(self, arguments):
        logger.debug(f"Full API request payload: {arguments}")

        try:
            handler = fal_client.submit(
                "fal-ai/flux-pro",
                arguments=arguments,
            )
            result = handler.get()
            logger.debug(f"API response: {result}")
            return result
        except Exception as e:
            logger.error(f"API error details: {str(e)}")
            if hasattr(e, 'response'):
                logger.error(f"API error response: {e.response.text}")
            raise RuntimeError(f"An error occurred when calling the fal.ai API: {str(e)}") from e

    def generate(self, **kwargs):
        arguments = self.prepare_arguments(**kwargs)
        result = self.call_api(arguments)
        output_images = self.process_images(result)
        return (output_images,)

NODE_CLASS_MAPPINGS = {
    "FalAPIFluxProNode": FalAPIFluxProNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FalAPIFluxProNode": "Fal API Flux Pro"
}