class sreya(Exception):
    pass
try:
    print("This is try block")
    raise sreya
except sreya:
    print("Sreya came to the classroom.")
print("End of the program.")
