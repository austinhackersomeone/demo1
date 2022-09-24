import platform


mysystem = platform.uname()


A1 = mysystem.system
A2 = mysystem.version
A3 = mysystem.release
A4 = mysystem.machine
A5 = mysystem.processor
A6 = mysystem.node



print(f"system OS = {A1}")
print(f"version =   {A2}")
print(f"release =   {A3}")
print(f"machine =   {A4}")
print(f"processor = {A5}")
print(f"Device =    {A6}")