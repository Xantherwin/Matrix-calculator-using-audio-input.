from audio import aud
import numpy as np 
from text2speech import ai

def matform():
    global rows
    global col

####rows
    print("Enter no. of rows: ")
    ai("Enter number of rows: ")
    temp_rows=aud()
        
    try:
        if (temp_rows=='tu'):
            temp_rows=2
        else:
            temp_rows=int(temp_rows)
            if isinstance(temp_rows, int):
                rows=temp_rows
                print(rows)
            else:
                print("\nThis is not a Number.")
                ai("\nSorry You have spoken something wrong, Please try again.")
                matform()
    except:
        print("\nTry again")
        matform()

####column    
    print("Enter no. of columns: ")
    ai("Enter number of columns: ")
    temp_col=aud()

    try:
        if (temp_col=='tu'):
            temp_col=2
        else:
            temp_col=int(temp_col)
            if isinstance(temp_col, int):
                col=temp_col
                print(col)
            else:
                print("This is not a Number.")
                ai("Sorry You have spoken something wrong, Please try again.")
                matform()
    except:
        print("Try again")
        matform()


def matin():
    #matrix input
    matrix = []
    for i in range(rows):
        row = []
        for j in range(col):
            def matin_1():
                print("Element ",i+1,j+1,": ")
                temp_element=aud()
                try:
                    temp_element=int(temp_element)
                    if isinstance(temp_element, int):
                        global element
                        element=temp_element
                        print(element)
                        return element
                    else:
                        print("This is not a Number.")
                        ai("Sorry You have spoken something wrong, You have to re-enter matrix.")
                except:
                    print("Try again")
                    matin_1()
                    
            matin_1()        
            row.append(element)
        matrix.append(row)
    print(np.array(matrix))
    return np.array(matrix)
