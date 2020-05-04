import mdl
from display import *
from matrix import *
from draw import *

knobCommands = ["move", "rotate", "scale", "set"]
threeDStuffs = ["box", "sphere", "torus"]

def dc(ary):
  return [x if type(x) is not list else dc(x) for x in ary]

def run(filename):
    """
    This function runs an mdl script
    """
    p = mdl.parseFile(filename)
    if p:
        (commands, symbols) = p
    else:
        print("Parsing failed.")
        return

    view = [0,
            0,
            1];
    ambient = [50,
               50,
               50]
    light = [[0.5,
              0.75,
              1],
             [255,
              255,
              255]]

    color = [0, 0, 0]
    tmp = new_matrix()
    ident( tmp )
    stack = [ [x[:] for x in tmp] ]
    #for when there are multiple coordinate systems
    stacks = []
    stacks.append(stack)
    screen = new_screen()
    zbuffer = new_zbuffer()
    tmp = []
    step_3d = 50
    consts = ''
    edges = []
    polygons = []
    symbols['.white'] = ['constants',
                         {'red': [0.2, 0.5, 0.5],
                          'green': [0.2, 0.5, 0.5],
                          'blue': [0.2, 0.5, 0.5]}]
    for i,command in enumerate(commands):
        c = command["op"]
        reflect = ".white"
        if c in knobCommands: knob = command["knob"]
        if c in threeDStuffs:
          const = command["constants"]
          if const != None: reflect = const
          if command["cs"] != None: pass
        args = command["args"]
        if c == "save":
          save_extension(screen, args[0] + ".png")
          print("Filename: " + args[0] + ".png")
          screen.clear()
        if c == "line":
          if command["cs0"] != None: pass
          if command["cs1"] != None: pass
          add_edge( edges,
                    float(args[0]), float(args[1]), float(args[2]),
                    float(args[3]), float(args[4]), float(args[5]) )
          matrix_mult(stack[-1], edges)
          draw_lines(edges, screen, zbuffer, color)
          edges = []
        if c == "curve": pass
        if c == "sphere":
          add_sphere(polygons,
                     float(args[0]), float(args[1]), float(args[2]),
                     float(args[3]), step_3d)
          matrix_mult(stack[-1], polygons)
          draw_polygons(polygons, screen, zbuffer, view, ambient, light, symbols, reflect)
          polygons = []
        if c == "box":
          add_box(polygons,
                     float(args[0]), float(args[1]), float(args[2]),
                     float(args[3]), float(args[4]), float(args[5]))
          matrix_mult(stack[-1], polygons)
          draw_polygons(polygons, screen, zbuffer, view, ambient, light, symbols, reflect)
          polygons = []
        if c == "torus":
          const = command["constants"]
          add_torus(polygons,
                     float(args[0]), float(args[1]), float(args[2]),
                     float(args[3]), float(args[4]), step_3d)
          matrix_mult(stack[-1], polygons)
          draw_polygons(polygons, screen, zbuffer, view, ambient, light, symbols, reflect)
          polygons = []
        if c == "pop":
          stack.pop()
        if c == "push":
          stack.append(dc(stack[-1]))
        if c == "move":
          if knob != None: pass
          t = make_translate(float(args[0]), float(args[1]), float(args[2]))
          matrix_mult(stack[-1], t)
          stack[-1] = dc(t)
        if c == "rotate":
          theta = float(args[1]) * (math.pi / 180)
          if args[0] == 'x':
              t = make_rotX(theta)
          elif args[0] == 'y':
              t = make_rotY(theta)
          else:
              t = make_rotZ(theta)
          matrix_mult(stack[-1], t)
          stack[-1] = dc(t)
        if c == "scale":
          t = make_scale(float(args[0]), float(args[1]), float(args[2]))
          matrix_mult(stack[-1], t)
          stack[-1] = dc(t)
        #it seems like the mdl.py file already does everything I need for constants
        if c == "constants": pass
        #to be coded later
        if c == "save_knobs": pass
        if c == "tween": pass
        if c == "light": pass
        if c == "mesh": pass
        if c == "basename": pass
