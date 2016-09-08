
def improved(A):

    A.sort()
    Array = A
    ini = 0
    fin = len(Array)-1
    cont = 0
    for i in range(fin):
        if Array[i]<0 :
           for j in range(fin):
                j = j+1
                der = fin
                if (Array[i]+Array[j])< 0:
                   lef = (j+1)
                   while lef <=der:
                     mid = (lef+der)/2
                     mid = int(mid)
                     if Array[mid] == -(Array[i]+Array[j]):
                        cont +=1
                        break
                     elif Array[mid] > -(Array[i]+Array[j]):
                        der = mid-1
                     else:
                        lef = mid+1

    return print ("tripletas suman : %s " %cont )



