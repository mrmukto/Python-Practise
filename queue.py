"""
queue , and there should be first in first out
"""
from collections import  deque
love = deque(["Amminur", "Mukt", "True"])
love.popleft()
print(love)
love.popleft()
love.popleft()
if not love:
    print("NOt any")