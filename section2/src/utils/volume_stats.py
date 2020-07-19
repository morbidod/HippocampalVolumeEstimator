"""
Contains various functions for computing statistics over 3D volumes
"""
import numpy as np

def Dice3d(a, b):
    """
    This will compute the Dice Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks -
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # TASK: Write implementation of Dice3D. If you completed exercises in the lessons
    # you should already have it.
    # <YOUR CODE HERE>
    #Dice Similarity coefficient
    #D=2*(X intercept Y)/(X+Y)
    intersection = 0
    for x in range(a.shape[0]):
        for y in range(a.shape[1]):
            for z in range(a.shape[2]):
                if (a[x,y,z]!=0 and b[x,y,z]!=0):
                    intersection = intersection + 1
    volumes = np.sum(a>0) + np.sum(b>0)
    if volumes == 0:
       return -1
    else:
        return 2.*float(intersection) / float(volumes)
    pass

def Jaccard3d(a, b):
    """
    This will compute the Jaccard Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks - 
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # TASK: Write implementation of Jaccard similarity coefficient. Please do not use 
    # the Dice3D function from above to do the computation ;)
    # <YOUR CODE GOES HERE>
    volumes=np.sum(a>0)+np.sum(b>0)
    
    intersection=0
    for x in range(a.shape[0]):
        for y in range(a.shape[1]):
            for z in range(a.shape[2]):
                if (a[x,y,z]!=0 and b[x,y,z]!=0):
                    intersection = intersection + 1
                 
    if volumes == 0:
       return -1
    else:
        jc=intersection/(volumes-intersection)   
        return jc
    pass
    
def check_value(a):
    print("check value Shape:",a.shape, "tot:",a.shape[0]*a.shape[1]*a.shape[2])
    print("Val 0:",np.count_nonzero(a==0))
    print("Val 1:",np.count_nonzero(a==1))
    print("Val 2:",np.count_nonzero(a==2))
    print("Sum:",np.sum(a), np.count_nonzero(a==0)+np.count_nonzero(a==1)+np.count_nonzero(a==2))
    pass