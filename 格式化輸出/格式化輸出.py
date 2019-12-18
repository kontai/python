name = "kontai"
print("My Name is %s" % name)

id = 12345
print("Id=%8d" % id)
print("Id=%.8d" % id)
print("Id=%08d" % id)

pi = 3.14159  # type: float
print("PI=%f" % pi)
print("PI=%.2f" % pi)
print("PI=%.3f" % pi)
print("PI=%06.3f" % pi)

print("*", end=" ")
print("*")

print("*", end="-")
print("*")

'{0}{1:.2f}'.format('Pi = ', 3.1415)
