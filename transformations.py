from matrix import *
import math

def sin(theta):
  return math.sin(math.radians(theta))

def cos(theta):
  return math.cos(math.radians(theta))

def scale(matrix, x, y, z):
  ident(matrix)
  matrix[0][0] = x
  matrix[1][1] = y
  matrix[2][2] = z

def translate(matrix, x, y, z):
  ident(matrix)
  matrix[0][3] = x
  matrix[1][3] = y
  matrix[2][3] = z

def rotate(matrix, direction, theta):
  ident(matrix)
  if direction == "x": rotateX(matrix, theta)
  elif direction == "y": rotateY(matrix, theta)
  else: rotateZ(matrix, theta)

def rotateX(matrix, theta):
  matrix[1][1] = cos(theta)
  matrix[1][2] = -1 * sin(theta)
  matrix[2][1] = sin(theta)
  matrix[2][2] = cos(theta)

def rotateY(matrix, theta):
  matrix[0][0] = cos(theta)
  matrix[2][0] = -1 * sin(theta)
  matrix[0][2] = sin(theta)
  matrix[2][2] = cos(theta)

def rotateZ(matrix, theta):
  matrix[1][1] = cos(theta)
  matrix[0][1] = -1 * sin(theta)
  matrix[1][0] = sin(theta)
  matrix[0][0] = cos(theta)
