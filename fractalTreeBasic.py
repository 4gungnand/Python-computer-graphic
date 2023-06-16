import turtle


def tree(branch_len, t):
    branches = []
    t.forward(branch_len)
    branches.append({'x': t.xcor(),
                     'y': t.ycor(),
                     'angle': t.heading()})
    while branch_len > 1:
        new_branches = []
        for branch in branches:
            t.up()
            t.goto(branch.get('x'), branch.get('y'))
            t.setheading(branch.get('angle'))
            t.down()
            t.right(20)
            t.forward(branch_len)
            new_branches.append({'x': t.xcor(),
                                 'y': t.ycor(),
                                 'angle': t.heading()})
            t.up()
            t.goto(branch.get('x'), branch.get('y'))
            t.down()
            t.left(40)
            t.forward(branch_len)
            new_branches.append({'x': t.xcor(),
                                 'y': t.ycor(),
                                 'angle': t.heading()})

        branches = new_branches
        branch_len -= 10


def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(40,t)
    my_win.exitonclick()


if __name__ == '__main__':
    main()
