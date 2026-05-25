str1 = "today is raining day"

# replace rain with sun
str2 = str1.replace("raining", "sunny")
print(str2)


# replace "rain " with "sunny "
# note: use a space after "rain" to avoid replacing "raining"
# return original string if not found
str3 = str1.replace("rain ", "sunny ")
print(str3)  # today is sunny day