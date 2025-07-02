# Search Algorithms Learning Path

## Core Learning Order

### Phase 1: Essential Searches (Week 1)
- **Linear Search**
  - Time: O(n)
  - Use when: Unsorted data
  - Practice: Implement with early exit condition

- **Binary Search** (🔥 Most Important)
  - Time: O(log n)
  - Must-learn variations:
    - Find first/last occurrence
    - Insert position
    - Search in rotated array
  - Common pitfalls: Off-by-one errors, overflow

- **Hash Table Search**
  - Python: `dict` and `set`
  - Time: O(1) average
  - Practice: Two Sum, duplicate detection

### Phase 2: Tree Search (Week 1-2)
- **BST Search**
  - Binary search adapted to trees
  - Time: O(h) (h = tree height)
  - Practice:
    - Validate BST
    - Find closest value

### Phase 3: Binary Search Variations (Week 2)
- **Advanced Binary Search**
  - Jump search (√n blocks)
  - Exponential search (unbounded arrays)
  - Interpolation search (uniform data)
  - Practice: Leetcode #702 (Search in Sorted Array)

### Phase 4: String Search (Optional)
- **Naive String Search**
  - Time: O(mn)
- **KMP Algorithm** (Advanced)
  - Partial match table
  - Time: O(n+m)

## Advanced/Optional (Learn As Needed)
- Ternary search (divide into 3)
- Fibonacci search (golden section)
- Sentinel linear search (optimization)

---

## Why This Order Works

### Interview Priority
| Algorithm          | Interview Frequency | Difficulty |
|--------------------|---------------------|------------|
| Binary Search      | ★★★★★               | Medium     |
| Hash Table Search  | ★★★★★               | Easy       |
| BST Search         | ★★★★☆               | Medium     |
| String Search      | ★★☆☆☆               | Hard       |

### Time Investment Guide
| Phase | Time Allocation | Key Focus |
|-------|-----------------|-----------|
| 1     | 60% effort      | Binary search mastery |
| 2     | 25% effort      | BST applications |
| 3-4   | 15% effort      | Niche cases |

---

## Learning Checklist

### Phase 1: Core
- [ ] Implement binary search from scratch
- [ ] Solve 5 binary search problems
- [ ] Master Python dictionary lookups

### Phase 2: Tree Search
- [ ] Implement BST search
- [ ] Solve 3 BST problems

### Phase 3: Variations
- [ ] Implement jump search
- [ ] Understand interpolation formula

### Phase 4: String
- [ ] Implement naive string search
- [ ] Study KMP partial match table

---

## Pro Tips

1. **When to Use What:**

Sorted array? → Binary search

Unsorted? → Linear or hash table

Tree structure? → BST search

Text patterns? → KMP (if performance critical)

2. **Avoid These Mistakes:**

Forgetting to sort before binary search

Infinite loops in BST search

Over-optimizing with exotic searches prematurely