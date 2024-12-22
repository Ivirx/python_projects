from PIL import Image, ImageDraw


def create_dot_grid(image_size=(2480, 3508), dot_size=5, spacing=50, output_file="a4_dot_grid.png", dpi=300):
    """
    Creates an image with a grid of dots, sized for A4 paper.

    Parameters:
        image_size (tuple): Size of the image in pixels (width, height).
        dot_size (int): Diameter of each dot.
        spacing (int): Space between the centers of the dots.
        output_file (str): Output file name for the image.
        dpi (int): DPI of the image for clarity in print.
    """
    # Create a blank white image
    img = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(img)

    # Calculate positions for the grid
    for y in range(spacing // 2, image_size[1], spacing):
        for x in range(spacing // 2, image_size[0], spacing):
            # Draw a circle (dot)
            draw.ellipse([
                (x - dot_size // 2, y - dot_size // 2),
                (x + dot_size // 2, y + dot_size // 2)
            ], fill="black")

    # Save the image with the correct DPI
    output_file = f'./dots/{output_file.split(".")[0]}_{dot_size}_{
        spacing}_{dpi}.png'
    img.save(output_file, dpi=(dpi, dpi))
    print(f"Dot grid image saved as {output_file} with size {
          image_size[0]}x{image_size[1]} pixels at {dpi} DPI.")


# Parameters to adjust
a4_size_pixels = (2480, 3508)   # A4 dimensions at 300 DPI
dot_size = 3                    # Diameter of dots
spacing = 80                    # Distance between dot centers

# Create the dot grid image for A4 paper
# create_dot_grid(image_size=a4_size_pixels, dot_size=dot_size, spacing=spacing)

for dot_size in [3, 5]:
    for spacing in range(10, 210, 10):
        create_dot_grid(
            image_size=a4_size_pixels, dot_size=dot_size, spacing=spacing
        )
