from mainc import m_aud
from audio import aud
import numpy as np
from matrix import matform as mf
from matrix import matin as mi
from text2speech import ai

print('''
Welcome to our Modern Matrix Calculator

Here are some operations which we can perform...
1. Addition
2. Subtraction
3. Multiplication
4. Transpose
5. Determinant
6. Adjoint
7. Inverse
8. Cofactor
''')
ai('''
Welcome to our Modern Matrix Calculator
Here are some operations which we can perform...
Addition
Subtraction
Multiplication
Transpose
Determinant
Adjoint
Inverse
Cofactor
''')

def mat_el3():
    global mat1
    global mat2
    print("Enter rows and columns for Matrix-1 and Matrix-2: ")
    ai("Enter rows and columns for Matrix-1 and Matrix-2: ")
    mf()
    print("\nEnter elements of Matrix-1:")
    ai("\nEnter elements of Matrix-1:")
    mat1=mi()
    print("\nEnter elements of Matrix-2:")
    ai("\nEnter elements of Matrix-2:")
    mat2=mi()

def mat_el5():
    global matx
    print("Enter rows and columns for Matrix: ")
    ai("Enter rows and columns for the Matrix: ")
    mf()
    print("\nEnter elements of Matrix:")
    ai("Enter elements of the Matrix:")
    matx=mi()

def start():
    m_choice=m_aud()
    m_choice=m_choice.lower()

    if(m_choice=="addition"):
        mat_el3()
        print("\nAddition of the Matrices is\n",np.add(mat1,mat2))
        
    elif(m_choice=='subtraction'):
        mat_el3()
        print("\nSubtraction of the Matrices is\n",np.subtract(mat1,mat2))
        
    elif(m_choice=='multiplication'):
        mat_el3()
        print("\nMultiplication of the Matrices is\n",np.dot(mat1,mat2))

    elif(m_choice=='transpose'):
        mat_el5()
        print("\nTranspose of matrix is:\n",np.transpose(matx))
        
    elif(m_choice=='determinant'):
        mat_el5()
        print("\nDeterminant of matrix is:\n",np.linalg.det(matx))
        
    elif(m_choice=='adjoint'):
        mat_el5()
        adjoint_mat=np.linalg.inv(matx).T * np.linalg.det(matx)
        print("\nAdjoint of matrix is:\n",np.transpose(adjoint_mat))
        
    elif(m_choice=='inverse'):
        mat_el5()
        print("\nInverse of matrix is:\n",np.linalg.inv(matx))
        
    elif(m_choice=='cofactor'):
        mat_el5()
        print("\nCofactor of matrix is:\n",np.linalg.inv(matx).T * np.linalg.det(matx))
        
    else:
        print("Sorry, you have spoken invalid operation. Try Again...")
        ai("Sorry, you have spoken invalid operation. Try Again...")
        start()

    ai('''Here is the result of your chosen operation.
        Thank you for using our matrix calculator''')
start()

