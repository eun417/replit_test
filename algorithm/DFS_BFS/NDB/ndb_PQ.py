#이코테 - DFS/BFS 실전문제(책 정답코드)

#3. 음료수 얼려 먹기
def solution1() :
  #N, M을 공백으로 구분하여 입력받기
  n, m = map(int, input().split())

  #2차원 리스트의 맵 정보 입력받기
  graph = []
  for i in range(n) :
    graph.append(list(map(int,input())))

  #DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
  def dfs(x, y) :
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m :
      return False
      
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0 :
      #해당 노드 방문 처리
      graph[x][y] = 1
      #상, 하, 좌, 우 위치도 모두 재귀적으로 호출 -> 연결된 모든 지점 방문
      dfs(x-1, y)
      dfs(x, y-1)
      dfs(x+1, y)
      dfs(x, y+1)
      return True
      
    return False

  #모든 노드(위치)에 대하여 음료수 채우기
  result = 0
  for i in range(n) :
    for j in range(m) :
      #현재 위치에서 DFS 수행
      if dfs(i, j) == True :  #방문하지 않은 지점 수를 셈
        result += 1
        
  print(result)  #정답 출력


#4. 미로 탈출
def solution2() :
  from collections import deque

  #N, M을 공백으로 구분하여 입력받기
  n, m = map(int, input().split())

  #2차원 리스트의 맵 정보 입력받기
  graph = []
  for i in range(n) :
    graph.append(list(map(int, input()))) 

  #이동할 네 방향 정의(상, 하, 좌, 우)
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  #BFS 소스코드 구현
  def bfs(x, y) :
    #큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    
    #큐가 빌 때까지 반복
    while queue :
      x, y = queue.popleft()
      #현재 위치에서 네 방향으로의 위치 확인
      for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        #미로 찾기 공간을 벗어난 경우 무시
        if nx < 0 or ny < 0 or nx >= n or ny >= m :
          continue
        #벽인 경우 무시
        if graph[nx][ny] == 0 :
          continue
        #해당 노드를 처음 방문하는 경우에만 최단 거리 기록
        if graph[nx][ny] == 1 :
          graph[nx][ny] = graph[x][y] + 1
          queue.append((nx, ny))

    #가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

  #BFS를 수행한 결과 출력
  print(bfs(0, 0))

  # for i in range(n) :
  #   for j in range(m) :
  #     print(graph[i][j], end = ' ')
  #   print()