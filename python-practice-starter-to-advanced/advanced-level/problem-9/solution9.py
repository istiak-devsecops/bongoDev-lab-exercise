from PIL import Image

def convert_to_grayscale(input_path, output_path):
    """
    Converts a color image to grayscale and saves it.

    Parameters:
    - input_path: str, path to the input color image
    - output_path: str, path to save the grayscale image
    """
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Convert to grayscale
        grayscale_img = img.convert("L")
        
        # Save the grayscale image
        grayscale_img.save(output_path)
        print(f"Grayscale image saved to {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")