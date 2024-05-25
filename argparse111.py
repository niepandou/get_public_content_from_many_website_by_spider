#可用于在命令行中执行时添加参数
import argparse
import math

def get_Cylinder(radius,height):
    return math.pi * (radius ** 2) * (height)

parser = argparse.ArgumentParser(description='Calculate volume of a cylinder')
parser.add_argument('radius',type=int,help='Radius of cylinder')
parser.add_argument('height',type=int,help='Height of cylinder')
#获取所有参数
args = parser.parse_args()
print(get_Cylinder(args.radius,args.height))