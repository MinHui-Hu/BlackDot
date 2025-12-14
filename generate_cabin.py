from PIL import Image, ImageDraw

# Create a new image with white background
img = Image.new('RGB', (200, 200), color='white')
draw = ImageDraw.Draw(img)

# Draw the cabin base (rectangle)
draw.rectangle([50, 100, 150, 180], fill='brown', outline='black')

# Draw the roof (triangle)
draw.polygon([(40, 100), (100, 50), (160, 100)], fill='red', outline='black')

# Draw a door
draw.rectangle([90, 130, 110, 180], fill='black')

# Draw windows
draw.rectangle([60, 120, 80, 140], fill='lightblue', outline='black')
draw.rectangle([120, 120, 140, 140], fill='lightblue', outline='black')

# Save the image
img.save('Logo/cabin.png')