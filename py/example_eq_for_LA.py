import plot_tool

def L1(x, y):
    return 2 * x - y

def L2(x, y):
    return -x + 2 * y

plot_tool.plot_implicit_functions([L1, L2], "Row Picture", [0, 3], ["$2x-y=0$", "$-x+2y=3$"], (-3, 3), (0, 6), "example equation for the essense of linear algebra", 24)