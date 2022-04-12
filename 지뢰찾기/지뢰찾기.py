row, col = map(int,input().split())  #/행열값 입력 받기
matrix = []                          #/이중배열을 만들기 위한 list
for i in range(row):
  matrix.append(list(input()))       #자리선정
for i in range(row):                 #만약 지뢰값이 없는 '.'구역에 진입시 주변 8칸 (i-1,i+2), (j-1,j+2)의 범위 내에서 '*'탐색후 있으면 count +=1
  for j in range(col):
    count = 0
    if matrix[i][j] == '.':
      for x in range(i-1,i+2):
        for y in range(j-1,j+2):
          if not (x < 0 or y < 0 or x >= row or y >= col):        #index가 범위 밖으로 나가지 않게 설정
            if matrix[x][y] == '*':
              count +=1
      matrix[i][j] = count
      print(matrix[i][j],end="")
    else:
      print(matrix[i][j],end="")
  print()
