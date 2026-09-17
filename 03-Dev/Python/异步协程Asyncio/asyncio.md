```python
import asyncio

asyncio def task(i):
    print(f"task {i} start")
    print(f"task {i} end")
    
loop = asyncio.get_event_loop()

tasks = [task(1),task(2)]
```

