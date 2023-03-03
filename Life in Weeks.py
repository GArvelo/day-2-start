age = input("What is your current age? ")
#Turn age into a int
a = int(age)
#result var equal to subtract age from 90
result = 90 - a
#Each var will be multiply by result
days = 365 * result
weeks = 52 * result
months= 12 * result

#F-strings provide a way to embed expressions inside string literals, using a minimal syntax. It should be noted that an f-string is really an expression evaluated at run time, not a constant value. In Python source code, an f-string is a literal string, prefixed with 'f', which contains expressions inside braces.
print(f"You have {days} days, {weeks} weeks, and {months} months left.")