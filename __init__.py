import nodes

class EmptyLatentImageFromImage(nodes.EmptyLatentImage):
	@classmethod
	def INPUT_TYPES(s):
		return {
			"required": { 
				"images": ("IMAGE", ),
				"batch_size": ("INT", {"default": 1, "min": 1, "max": 4096, "tooltip": "The number of latent images in the batch."})
			}
		}
	RETURN_TYPES = ("LATENT",)
	OUTPUT_TOOLTIPS = ("The empty latent image batch.",)
	FUNCTION = "generate"

	CATEGORY = "latent"
	DESCRIPTION = "Create a new batch of empty latent images to be denoised via sampling."

	def generate(self, images, batch_size=1):
		image = images[0]
		return super().generate(image.shape[2], image.shape[1], batch_size)

class EmptyImageFromImage(nodes.EmptyImage):

	@classmethod
	def INPUT_TYPES(s):
		return {
			"required": {
				"images": ("IMAGE", ),
				"batch_size": ("INT", {"default": 1, "min": 1, "max": 4096}),
				"color": ("INT", {"default": 0, "min": 0, "max": 0xFFFFFF, "step": 1, "display": "color"}),
			}
		}
	RETURN_TYPES = ("IMAGE",)
	FUNCTION = "generate"

	CATEGORY = "image"

	def generate(self, images, batch_size=1, color=0):
		image = images[0] if len(image) > 1 else images
		return super().generate(image.shape[2], image.shape[1], batch_size, color)

NODE_CLASS_MAPPINGS = {
	"EmptyLatentImageFromImage" : EmptyLatentImageFromImage,
	"EmptyImageFromImage": EmptyImageFromImage,
}

__all__ = ['NODE_CLASS_MAPPINGS']
