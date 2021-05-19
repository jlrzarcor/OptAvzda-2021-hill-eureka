import numpy as np


def cgm(A,b,x,tolerance=1e-7, iter=1000):
    """
    given a system of linear equation returns the coefficient matrix optimized      
        
        input:
            A: Coeficient matrix
            b: solution vector
            x: vector to be optimize
        output:
            x: vector optimized
    """
    r = np.dot(A,x)-b
    p = -r
    k = 0
    
    while True: 
        r_s = np.dot(np.transpose(r),r)
        alpha_k = r_s/np.dot(np.transpose(p),np.dot(A,p))
        
        x = x + np.dot(alpha_k,p)
        
        r = r + np.dot(alpha_k, np.dot(A,p))
        
        beta = np.dot(np.transpose(r),r)/r_s
        
        p = -r + beta*p
        
        k =+ 1
        if np.linalg.norm(r) < tolerance:
            break
        if k > iter:
            break    
    return x


def its_simetric(matrix):
    """
    ckecks if a matrix is symmetric

        inputs:
            matrix[array]: a cuadratic matix
        outputs:
            True if our matrix is simetric, False otherwise
    """
    matrix_t = np.transpose(matrix)
    return matrix.all() == matrix_t.all()


def symmetrize_posdef(n):
    """
    creates positive define nxn arrays

    input:
        n[integer]: size of the symmetric matrix required
    optput:
        a[array]:symetric define positive matix
    """
    while True:

        a = np.random.randint(99, size=(n,n))
        if np.all(np.linalg.eigvals(a) > 0):
            break
        else:
            a = np.random.randint(10, size=(n,n))
            
    return a

def is_pos_def(x):
    """
    ckecks if a matrix is define positive

        input:
            x[array]: matrix to check if it  is define positive
        output:
            True if the matix is define positive and False otherwise
            
    """
    return np.all(np.linalg.eigvals(x) > 0)
