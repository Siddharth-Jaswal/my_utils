
from collections import deque
from typing import Deque, Any, Optional

class Stack:
    def __init__(self) -> None:
        self.stack: Deque[Any] = deque()

    def empty(self) -> bool:
        """Return True if stack is empty."""
        return not self.stack

    def push(self, ele: Any) -> bool:
        """Push an element and return True if successful."""
        try:
            self.stack.append(ele)
            return True
        except Exception as e:
            print(f"Error while pushing: {e}")
            return False

    def pop(self) -> Optional[Any]:
        """Pop top element; return None if stack is empty."""
        return self.stack.pop() if self.stack else None

    def top(self) -> Optional[Any]:
        """Return top element; return None if stack is empty."""
        return self.stack[-1] if self.stack else None