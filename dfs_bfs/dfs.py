def dfs(visited, now, data):
    if (visited[now] == True):
        return
    visited[now] = True
    print(now, end=" ")
    for search in data[now]:
        if not visited[search]:
            dfs(visited, search, data)
    return