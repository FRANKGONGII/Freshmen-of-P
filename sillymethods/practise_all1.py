print("Let's practice everything now")
print("You \' need to know \' bout escapes with \\ that do \n new lines and \t tabs")
poem = """
\t The lovely world 
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t where there is none
"""
print(".............")
print(poem)
print(">>>>>>>>>>>>")
five = 10 - 2 + 3 - 6
print("This should be five : %s " % five)


def secret_formula(started):
    jelly_beans = started * 50
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


started_point = 10000
beans, jars, crates = secret_formula(started_point)
print("We've %d beans, %d jars, and %d crates" % (beans, jars, crates))
started_point /= 10
print("we can do this too")
print("We've %d beans, %d jars, and %d crates" % (beans, jars, crates))


