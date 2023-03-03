height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#Code I created
h = float(height)
w = int(weight)

print(int(w /(h ** 2)))

#great example with explanations

#Using the exponent operator
bmi = weight_as_int / height_as_float **2
# or using multiplication and PEMDA
bmi = weight_as_in / (height_as_float * height_as_float)

bmi_as_int = int(bmi)

print(bmi_as_int)