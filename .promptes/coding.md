# Advanced Coding Mastery Guide for AI Development

## Table of Contents
1. [Advanced Programming Instructions](#advanced-programming-instructions)
2. [Algorithmic Problem-Solving Methodologies](#algorithmic-problem-solving-methodologies)
3. [Complex Data Structures Mastery](#complex-data-structures-mastery)
4. [Optimized and Maintainable Code Practices](#optimized-and-maintainable-code-practices)
5. [Progressive Algorithmic Logic Exercises](#progressive-algorithmic-logic-exercises)

---

## Advanced Programming Instructions

### Core Programming Principles

#### 1. Computational Thinking Framework
- **Decomposition**: Break complex problems into smaller, manageable components
- **Pattern Recognition**: Identify recurring patterns and abstract common solutions
- **Abstraction**: Focus on essential features while hiding implementation details
- **Algorithm Design**: Create step-by-step solutions with optimal efficiency

#### 2. Advanced Code Architecture
```python
# Example: Sophisticated class design with design patterns
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Protocol

T = TypeVar('T')

class Strategy(Protocol[T]):
    def execute(self, data: T) -> T:
        ...

class Context(Generic[T]):
    def __init__(self, strategy: Strategy[T]):
        self._strategy = strategy
    
    def set_strategy(self, strategy: Strategy[T]) -> None:
        self._strategy = strategy
    
    def execute_strategy(self, data: T) -> T:
        return self._strategy.execute(data)
```

#### 3. Memory Management and Performance Optimization
- **Memory Profiling**: Use tools like `memory_profiler`, `tracemalloc`
- **Lazy Evaluation**: Implement generators and iterators for large datasets
- **Caching Strategies**: Implement memoization and LRU caches
- **Garbage Collection**: Understand reference counting and cycle detection

### Advanced Language Features

#### Python Advanced Concepts
```python
# Metaclasses for dynamic class creation
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# Descriptors for attribute access control
class ValidatedAttribute:
    def __init__(self, validator):
        self.validator = validator
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        if self.validator(value):
            obj.__dict__[self.name] = value
        else:
            raise ValueError(f"Invalid value for {self.name}")

# Context managers for resource management
class DatabaseConnection:
    def __enter__(self):
        self.connection = self.connect()
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        return False
```

---

## Algorithmic Problem-Solving Methodologies

### 1. Systematic Problem Analysis

#### Problem Decomposition Framework
1. **Input Analysis**: Identify data types, constraints, and edge cases
2. **Output Requirements**: Define expected results and format
3. **Constraint Mapping**: Understand time/space complexity requirements
4. **Pattern Identification**: Recognize problem categories (DP, Graph, etc.)

#### Example: Complex Problem Breakdown
```python
def solve_complex_problem(input_data):
    """
    Problem: Find the longest increasing subsequence with maximum sum
    
    Analysis:
    - Input: Array of integers
    - Output: Maximum sum of increasing subsequence
    - Constraints: O(n²) time acceptable, O(n) space preferred
    - Pattern: Dynamic Programming with optimization
    """
    
    # Step 1: Initialize DP arrays
    n = len(input_data)
    dp_length = [1] * n  # Length of LIS ending at i
    dp_sum = input_data[:]  # Sum of LIS ending at i
    
    # Step 2: Fill DP tables
    for i in range(1, n):
        for j in range(i):
            if input_data[j] < input_data[i]:
                if dp_length[j] + 1 > dp_length[i]:
                    dp_length[i] = dp_length[j] + 1
                    dp_sum[i] = dp_sum[j] + input_data[i]
                elif (dp_length[j] + 1 == dp_length[i] and 
                      dp_sum[j] + input_data[i] > dp_sum[i]):
                    dp_sum[i] = dp_sum[j] + input_data[i]
    
    return max(dp_sum)
```

### 2. Advanced Algorithm Design Patterns

#### Dynamic Programming Mastery
```python
# State Space Reduction Technique
def optimized_knapsack(weights, values, capacity):
    """
    Space-optimized 0/1 Knapsack using rolling array
    Time: O(n*W), Space: O(W) instead of O(n*W)
    """
    prev = [0] * (capacity + 1)
    
    for i in range(len(weights)):
        curr = [0] * (capacity + 1)
        for w in range(capacity + 1):
            # Don't take item i
            curr[w] = prev[w]
            
            # Take item i if possible
            if w >= weights[i]:
                curr[w] = max(curr[w], prev[w - weights[i]] + values[i])
        
        prev = curr
    
    return prev[capacity]

# Memoization with Custom Hash
from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def complex_recursion(self, state_tuple):
        """
        Use tuples for hashable state representation
        in complex recursive problems
        """
        if self.is_base_case(state_tuple):
            return self.base_result(state_tuple)
        
        results = []
        for next_state in self.generate_next_states(state_tuple):
            results.append(self.complex_recursion(next_state))
        
        return self.combine_results(results)
```

#### Graph Algorithm Sophistication
```python
from collections import defaultdict, deque
import heapq

class AdvancedGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.weights = {}
    
    def dijkstra_with_path(self, start, end):
        """
        Dijkstra's algorithm returning both distance and path
        """
        distances = {start: 0}
        previous = {}
        pq = [(0, start)]
        visited = set()
        
        while pq:
            current_dist, current = heapq.heappop(pq)
            
            if current in visited:
                continue
                
            visited.add(current)
            
            if current == end:
                # Reconstruct path
                path = []
                while current is not None:
                    path.append(current)
                    current = previous.get(current)
                return distances[end], path[::-1]
            
            for neighbor in self.graph[current]:
                weight = self.weights[(current, neighbor)]
                distance = current_dist + weight
                
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current
                    heapq.heappush(pq, (distance, neighbor))
        
        return float('inf'), []
    
    def strongly_connected_components(self):
        """
        Tarjan's algorithm for finding SCCs
        """
        index_counter = [0]
        stack = []
        lowlinks = {}
        index = {}
        on_stack = {}
        sccs = []
        
        def strongconnect(node):
            index[node] = index_counter[0]
            lowlinks[node] = index_counter[0]
            index_counter[0] += 1
            stack.append(node)
            on_stack[node] = True
            
            for neighbor in self.graph[node]:
                if neighbor not in index:
                    strongconnect(neighbor)
                    lowlinks[node] = min(lowlinks[node], lowlinks[neighbor])
                elif on_stack[neighbor]:
                    lowlinks[node] = min(lowlinks[node], index[neighbor])
            
            if lowlinks[node] == index[node]:
                component = []
                while True:
                    w = stack.pop()
                    on_stack[w] = False
                    component.append(w)
                    if w == node:
                        break
                sccs.append(component)
        
        for node in self.graph:
            if node not in index:
                strongconnect(node)
        
        return sccs
```

---

## Complex Data Structures Mastery

### 1. Advanced Tree Structures

#### Self-Balancing Trees
```python
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        
        return x
    
    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y
    
    def insert(self, root, key):
        # Standard BST insertion
        if not root:
            return AVLNode(key)
        
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root  # Duplicate keys not allowed
        
        # Update height
        root.height = 1 + max(self.get_height(root.left), 
                             self.get_height(root.right))
        
        # Get balance factor
        balance = self.get_balance(root)
        
        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        
        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        
        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        
        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        
        return root
```

#### Segment Trees for Range Queries
```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def push(self, node, start, end):
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node] * (end - start + 1)
            if start != end:
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            self.lazy[node] = 0
    
    def update_range(self, node, start, end, l, r, val):
        self.push(node, start, end)
        if start > r or end < l:
            return
        
        if start >= l and end <= r:
            self.lazy[node] += val
            self.push(node, start, end)
            return
        
        mid = (start + end) // 2
        self.update_range(2 * node + 1, start, mid, l, r, val)
        self.update_range(2 * node + 2, mid + 1, end, l, r, val)
        
        self.push(2 * node + 1, start, mid)
        self.push(2 * node + 2, mid + 1, end)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def query_range(self, node, start, end, l, r):
        if start > r or end < l:
            return 0
        
        self.push(node, start, end)
        
        if start >= l and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_sum = self.query_range(2 * node + 1, start, mid, l, r)
        right_sum = self.query_range(2 * node + 2, mid + 1, end, l, r)
        return left_sum + right_sum
```

### 2. Advanced Hash Structures

#### Bloom Filters for Probabilistic Membership
```python
import hashlib
from bitarray import bitarray

class BloomFilter:
    def __init__(self, capacity, error_rate):
        self.capacity = capacity
        self.error_rate = error_rate
        self.bit_array_size = self._get_size()
        self.hash_count = self._get_hash_count()
        self.bit_array = bitarray(self.bit_array_size)
        self.bit_array.setall(0)
    
    def _get_size(self):
        import math
        size = -(self.capacity * math.log(self.error_rate)) / (math.log(2) ** 2)
        return int(size)
    
    def _get_hash_count(self):
        import math
        count = (self.bit_array_size / self.capacity) * math.log(2)
        return int(count)
    
    def _hash(self, item, seed):
        hash_obj = hashlib.md5((str(item) + str(seed)).encode())
        return int(hash_obj.hexdigest(), 16) % self.bit_array_size
    
    def add(self, item):
        for i in range(self.hash_count):
            index = self._hash(item, i)
            self.bit_array[index] = 1
    
    def check(self, item):
        for i in range(self.hash_count):
            index = self._hash(item, i)
            if self.bit_array[index] == 0:
                return False
        return True
```

---

## Optimized and Maintainable Code Practices

### 1. Performance Optimization Techniques

#### Algorithmic Optimization
```python
# Example: Optimizing nested loops with mathematical insights
def count_pairs_naive(arr, target):
    """O(n²) solution"""
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                count += 1
    return count

def count_pairs_optimized(arr, target):
    """O(n) solution using hash map"""
    count = 0
    seen = {}
    
    for num in arr:
        complement = target - num
        if complement in seen:
            count += seen[complement]
        
        seen[num] = seen.get(num, 0) + 1
    
    return count

# Bit manipulation for optimization
def count_set_bits_optimized(n):
    """Brian Kernighan's algorithm: O(number of set bits)"""
    count = 0
    while n:
        n &= n - 1  # Remove the rightmost set bit
        count += 1
    return count
```

#### Memory Optimization Patterns
```python
# Generator for memory-efficient processing
def process_large_dataset(filename):
    """Process large files without loading everything into memory"""
    def read_chunks(file_obj, chunk_size=8192):
        while True:
            chunk = file_obj.read(chunk_size)
            if not chunk:
                break
            yield chunk
    
    with open(filename, 'r') as file:
        for chunk in read_chunks(file):
            # Process chunk
            yield process_chunk(chunk)

# Object pooling for expensive object creation
class ObjectPool:
    def __init__(self, create_func, reset_func, initial_size=10):
        self.create_func = create_func
        self.reset_func = reset_func
        self.pool = [create_func() for _ in range(initial_size)]
        self.in_use = set()
    
    def acquire(self):
        if self.pool:
            obj = self.pool.pop()
        else:
            obj = self.create_func()
        
        self.in_use.add(obj)
        return obj
    
    def release(self, obj):
        if obj in self.in_use:
            self.in_use.remove(obj)
            self.reset_func(obj)
            self.pool.append(obj)
```

### 2. Code Maintainability Principles

#### SOLID Principles Implementation
```python
# Single Responsibility Principle
class EmailValidator:
    def validate(self, email):
        return '@' in email and '.' in email

class UserRegistration:
    def __init__(self, validator):
        self.validator = validator
    
    def register_user(self, email, password):
        if not self.validator.validate(email):
            raise ValueError("Invalid email")
        # Registration logic here

# Open/Closed Principle
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Credit card processing logic
        pass

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # PayPal processing logic
        pass

# Dependency Inversion Principle
class DatabaseInterface(ABC):
    @abstractmethod
    def save(self, data):
        pass

class UserService:
    def __init__(self, database: DatabaseInterface):
        self.database = database
    
    def create_user(self, user_data):
        # Business logic
        self.database.save(user_data)
```

#### Advanced Error Handling
```python
import logging
from contextlib import contextmanager
from typing import Optional, Union

class CustomException(Exception):
    def __init__(self, message: str, error_code: int = None):
        super().__init__(message)
        self.error_code = error_code
        self.timestamp = datetime.now()

@contextmanager
def error_handler(operation_name: str):
    """Context manager for consistent error handling"""
    try:
        logging.info(f"Starting operation: {operation_name}")
        yield
        logging.info(f"Completed operation: {operation_name}")
    except CustomException as e:
        logging.error(f"Custom error in {operation_name}: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error in {operation_name}: {e}")
        raise CustomException(f"Operation {operation_name} failed", 500)

# Retry mechanism with exponential backoff
import time
import random
from functools import wraps

def retry_with_backoff(max_retries=3, base_delay=1, max_delay=60):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise
                    
                    delay = min(base_delay * (2 ** attempt) + random.uniform(0, 1), max_delay)
                    logging.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay:.2f}s")
                    time.sleep(delay)
            
            return None
        return wrapper
    return decorator
```

---

## Progressive Algorithmic Logic Exercises

### Level 1: Foundation Building

#### Exercise 1: Advanced Array Manipulation
```python
def solve_array_challenge():
    """
    Problem: Given an array, find all subarrays with sum equal to target
    Constraints: O(n) time complexity required
    
    Example: arr = [1, 4, 20, 3, 10, 5], target = 33
    Output: [[20, 3, 10], [1, 4, 20, 3, 5]] (if exists)
    """
    
    def find_subarrays_with_sum(arr, target):
        result = []
        n = len(arr)
        
        # Use sliding window technique
        for start in range(n):
            current_sum = 0
            for end in range(start, n):
                current_sum += arr[end]
                
                if current_sum == target:
                    result.append(arr[start:end+1])
                elif current_sum > target:
                    break
        
        return result
    
    # Test implementation
    test_cases = [
        ([1, 4, 20, 3, 10, 5], 33),
        ([1, 4, 0, 0, 3, 10, 5], 7),
        ([1, 4], 0)
    ]
    
    for arr, target in test_cases:
        result = find_subarrays_with_sum(arr, target)
        print(f"Array: {arr}, Target: {target}, Result: {result}")

# Challenge: Optimize to O(n) using prefix sums and hash map
```

### Level 2: Intermediate Complexity

#### Exercise 2: Dynamic Programming Mastery
```python
def advanced_dp_challenge():
    """
    Problem: Minimum cost to make array palindrome
    Operations: Insert, delete, or replace characters
    Each operation has different costs
    """
    
    def min_cost_palindrome(s, insert_cost, delete_cost, replace_cost):
        n = len(s)
        # dp[i][j] = min cost to make s[i:j+1] palindrome
        dp = [[float('inf')] * n for _ in range(n)]
        
        # Base case: single characters are palindromes
        for i in range(n):
            dp[i][i] = 0
        
        # Fill for substrings of length 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    # Try all operations
                    # Replace s[i] with s[j] or vice versa
                    dp[i][j] = min(dp[i][j], dp[i + 1][j - 1] + replace_cost)
                    
                    # Delete s[i]
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + delete_cost)
                    
                    # Delete s[j]
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + delete_cost)
                    
                    # Insert character
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + insert_cost)
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + insert_cost)
        
        return dp[0][n - 1]
    
    # Test with various cost configurations
    test_string = "abcdef"
    result = min_cost_palindrome(test_string, 1, 1, 2)
    print(f"Minimum cost to make '{test_string}' palindrome: {result}")
```

### Level 3: Advanced Problem Solving

#### Exercise 3: Complex Graph Algorithms
```python
def advanced_graph_challenge():
    """
    Problem: Find the shortest path in a graph with negative weights
    but no negative cycles, and return the path reconstruction
    """
    
    class GraphSolver:
        def __init__(self):
            self.graph = defaultdict(list)
        
        def add_edge(self, u, v, weight):
            self.graph[u].append((v, weight))
        
        def bellman_ford_with_path(self, start, end, vertices):
            # Initialize distances and predecessors
            distances = {v: float('inf') for v in vertices}
            predecessors = {v: None for v in vertices}
            distances[start] = 0
            
            # Relax edges repeatedly
            for _ in range(len(vertices) - 1):
                for u in vertices:
                    if distances[u] != float('inf'):
                        for v, weight in self.graph[u]:
                            if distances[u] + weight < distances[v]:
                                distances[v] = distances[u] + weight
                                predecessors[v] = u
            
            # Check for negative cycles
            for u in vertices:
                if distances[u] != float('inf'):
                    for v, weight in self.graph[u]:
                        if distances[u] + weight < distances[v]:
                            raise ValueError("Graph contains negative cycle")
            
            # Reconstruct path
            path = []
            current = end
            while current is not None:
                path.append(current)
                current = predecessors[current]
            
            if path[-1] != start:
                return float('inf'), []  # No path exists
            
            return distances[end], path[::-1]
    
    # Test the implementation
    solver = GraphSolver()
    vertices = ['A', 'B', 'C', 'D', 'E']
    
    # Add edges with weights (including negative)
    edges = [
        ('A', 'B', -1), ('A', 'C', 4),
        ('B', 'C', 3), ('B', 'D', 2),
        ('B', 'E', 2), ('D', 'B', 1),
        ('D', 'C', 5), ('E', 'D', -3)
    ]
    
    for u, v, w in edges:
        solver.add_edge(u, v, w)
    
    distance, path = solver.bellman_ford_with_path('A', 'D', vertices)
    print(f"Shortest distance from A to D: {distance}")
    print(f"Path: {' -> '.join(path)}")
```

### Level 4: Expert-Level Challenges

#### Exercise 4: Advanced Data Structure Design
```python
def design_advanced_data_structure():
    """
    Problem: Design a data structure that supports:
    1. Insert(x): Insert element x
    2. Delete(x): Delete element x
    3. GetRandom(): Return random element in O(1)
    4. GetMedian(): Return median in O(1)
    """
    
    import random
    import heapq
    
    class AdvancedDataStructure:
        def __init__(self):
            self.elements = {}  # value -> index mapping
            self.array = []     # for O(1) random access
            self.max_heap = []  # for median (smaller half)
            self.min_heap = []  # for median (larger half)
        
        def insert(self, x):
            if x in self.elements:
                return False  # Duplicate
            
            # Add to array for random access
            self.array.append(x)
            self.elements[x] = len(self.array) - 1
            
            # Add to heaps for median calculation
            if not self.max_heap or x <= -self.max_heap[0]:
                heapq.heappush(self.max_heap, -x)
            else:
                heapq.heappush(self.min_heap, x)
            
            # Balance heaps
            self._balance_heaps()
            return True
        
        def delete(self, x):
            if x not in self.elements:
                return False
            
            # Remove from array (swap with last element)
            index = self.elements[x]
            last_element = self.array[-1]
            
            self.array[index] = last_element
            self.elements[last_element] = index
            
            self.array.pop()
            del self.elements[x]
            
            # Remove from heaps (lazy deletion)
            self._remove_from_heaps(x)
            return True
        
        def get_random(self):
            if not self.array:
                return None
            return random.choice(self.array)
        
        def get_median(self):
            if not self.max_heap and not self.min_heap:
                return None
            
            if len(self.max_heap) > len(self.min_heap):
                return -self.max_heap[0]
            elif len(self.min_heap) > len(self.max_heap):
                return self.min_heap[0]
            else:
                return (-self.max_heap[0] + self.min_heap[0]) / 2
        
        def _balance_heaps(self):
            if len(self.max_heap) > len(self.min_heap) + 1:
                element = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, element)
            elif len(self.min_heap) > len(self.max_heap) + 1:
                element = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -element)
        
        def _remove_from_heaps(self, x):
            # Implementation would require more complex heap operations
            # This is a simplified version
            pass
    
    # Test the data structure
    ds = AdvancedDataStructure()
    
    # Test operations
    operations = [
        ('insert', 1), ('insert', 2), ('insert', 3),
        ('get_median',), ('get_random',),
        ('delete', 2), ('get_median',)
    ]
    
    for op in operations:
        if op[0] == 'insert':
            result = ds.insert(op[1])
            print(f"Insert {op[1]}: {result}")
        elif op[0] == 'delete':
            result = ds.delete(op[1])
            print(f"Delete {op[1]}: {result}")
        elif op[0] == 'get_median':
            result = ds.get_median()
            print(f"Median: {result}")
        elif op[0] == 'get_random':
            result = ds.get_random()
            print(f"Random: {result}")
```

### Continuous Learning Framework

#### Self-Assessment Metrics
1. **Time Complexity Analysis**: Can you determine and optimize algorithmic complexity?
2. **Space Optimization**: Do you consider memory usage in your solutions?
3. **Edge Case Handling**: Are you identifying and handling corner cases?
4. **Code Readability**: Is your code self-documenting and maintainable?
5. **Testing Strategy**: Do you write comprehensive tests for your solutions?

#### Advanced Practice Recommendations
1. **Competitive Programming**: Participate in contests (Codeforces, AtCoder)
2. **System Design**: Study large-scale system architecture
3. **Code Review**: Analyze and critique existing codebases
4. **Performance Profiling**: Use tools to identify bottlenecks
5. **Algorithm Research**: Study cutting-edge algorithmic research papers

---

## Conclusion

This guide provides a comprehensive framework for developing advanced programming skills. The key to mastery lies in:

1. **Consistent Practice**: Regular problem-solving with increasing complexity
2. **Pattern Recognition**: Identifying common algorithmic patterns
3. **Optimization Mindset**: Always considering time/space trade-offs
4. **Code Quality**: Writing maintainable, readable, and efficient code
5. **Continuous Learning**: Staying updated with new techniques and best practices

Remember: Advanced programming is not just about knowing algorithms—it's about applying them effectively, writing clean code, and solving real-world problems efficiently.