class Matrix:
    def __init__(self, INFO):
        self.n = INFO[0]
        self.m = INFO[1]
        self.lines = INFO[2]
        self.columns = INFO[3]
    def getMatrixInfo(self):
        return [self.n, self.m, self.lines, self.columns]
    def printMatrix(self):
        print()
        for i in range(self.n):
            print(" ".join(str(self.lines[i][j]) for j in range(self.m)))


def dotProduct(SEQ1 = [], SEQ2 = []):
    SUM = 0
    for i in range(len(SEQ1)):
        SUM += SEQ1[i] * SEQ2[i]
    return SUM

def getTransposeMatrix(N, M, LINES):
    COLUMNS = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            COLUMNS[i][j] = LINES[j][i]
    return COLUMNS

def multiplyMatrix(A, B):
    LINES = [[] for i in range(A.n)]
    if A.m != B.n:
        return "Esta multiplicação não está definida."
    for i in range(A.n):
        for j in range(B.m):
            LINES[i].append(dotProduct(A.lines[i], B.columns[j]))
    return getMatrixInfo(A.n, B.m, LINES)

def sumMatrix(A, B, SIGN = False):
    LINES = A.lines
    if A.n != B.n or A.m != B.m:
        print("Esta " + "adição"*(not SIGN) + "diferença"*(SIGN) + " não está definida.")
        return getMatrixInfo(0, 0, [])
    for i in range(A.n):
        for j in range(A.m):
            LINES[i][j] += B.lines[i][j]*int(((not SIGN) - 0.5)*2)
    return getMatrixInfo(A.n, B.n, LINES)
            
def getMatrixInfo(N, M, LINES):
    return [N, M, LINES, getTransposeMatrix(N, M, LINES)]

def getMatrixInfoFromUser():
    N, M = map(int, input().split())
    LINES = [[0 for _ in range(M)] for _ in range(N)]
    INPUT_LIST = []
    for i in range(N):
        INPUT_LIST = list(map(int, input().split()))
        for j in range(len(INPUT_LIST)):
            LINES[i][j] = INPUT_LIST[j]
    COLUMNS = getTransposeMatrix(N, M, LINES)
    return [N, M, LINES, COLUMNS]

'''

D = Matrix(getMatrixInfoFromUser())
D.printMatrix()

'''

'''

A = Matrix(getMatrixInfoFromUser())
print(A.getMatrixInfo())
B = Matrix(getMatrixInfoFromUser())
print(B.getMatrixInfo())

x = int(input())

if x == 0:
    C = Matrix(multiplyMatrix(A, B))
elif x == 1:
    C = Matrix(sumMatrix(A, B))
else:
    C = Matrix(sumMatrix(A, B, True))

print(C.getMatrixInfo())

'''