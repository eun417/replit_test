#위에서 아래로 (교재 코드)
#N 입력받기
n = int(input())

#N개의 정수를 입력받아 리스트에 저장
array = []
for i in range(n):
  array.append(int(input()))

#파이썬 기본 정렬 라이브러리 이용하여 정렬 수행
array = sorted(array, reverse=True)

#정렬이 수행된 결과 출력
for i in array:
  print(i, end=' ')