"""
 Problem Statement:
 exercise 1 tutorial, we have to create a dictionary similar to the real-world dictionary.
 There is no limit to the definition provide to any word.

 The details and functionalities that are essential and must be present are:

 The user will give the word as input. Suppose that the word is present in your dictionary along with its definition or meaning.
 The program will print the meaning or definition of that word.

"""

Dict = {"ignore":"refuse to take notice of or acknowledge", "abandon":"cease to support or look after",
        "exaggerate":"enlarged or altered beyond normal proportions", "prejudice":"preconceived opinion that is not based on reason or actual experience", "programming":"the process of writing computer programs"}
print("Enter the Word")
Data1 = input()
print(Data1, "means", Dict[Data1])

