import turtle

tree_segments = ((50, 20), (80, 0), (120, -30), (150, -60))
stump_segments= ((50, 20), (80, 0), (120, -30), (150, -60))

window = turtle.Screen()
window.bgcolor("lightblue")


tree = turtle.Turtle()
tree.color("forest green")


def make_tree_segment(size, top_position):
    tree.begin_fill()
    tree.setposition(0, top_position)
    tree.setposition(size, top_position - size)
    tree.setposition(-size, top_position - size)
    tree.setposition(0, top_position)
    tree.end_fill()

for size, top_position in tree_segments:
   make_tree_segment(size, top_position)

turtle.done()