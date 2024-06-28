# Create a function area(sizes).
# sizes is a dictionary with 2 keys - width and height if the keys not exists the default value should be 1.
# The expected output should be the area size - width * height.

def area(sizes):
    width = sizes.get('width', 1) # if width does not exist in sizes it'd print 1
    height = sizes.get('height', 1)
    return width * height

print(area({'width': 5, 'height': 3}))