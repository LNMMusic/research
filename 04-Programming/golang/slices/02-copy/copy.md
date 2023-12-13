# Documentation: Slicing in Go - Making Copies and References

Slices are a key data type in Go, offering flexible and dynamic handling of sequences of data. Understanding how to create copies and references of slices is essential for managing data effectively in Go.

## Introduction to Slices

A slice is a segment of an array and provides a way to access a sequence of elements. It is composed of three components: a pointer to the array, the length of the segment, and its capacity.

## Creating Copies and References of Slices

### Shallow Copy

- **Definition**: A shallow copy of a slice is a new slice variable that points to the same underlying array as the original slice.
- **Characteristics**: 
  - Both the original and shallow copy share the same underlying array.
  - Modifications to the elements of one slice will be reflected in the other.

#### Example of Shallow Copy

```go
slShallowCopy := sl
```

In your code, `slShallowCopy` is a shallow copy of `sl`. Both point to the same underlying array.

### Deep Copy

- **Definition**: A deep copy of a slice involves creating a new underlying array and copying the elements from the original slice to this new array.
- **Characteristics**:
  - The original slice and the deep copy do not share the same underlying array.
  - Modifications to one slice will not affect the other.

#### Example of Deep Copy

```go
slDeepCopy := make([]int, len(sl))
copy(slDeepCopy, sl)
```

In this example, `slDeepCopy` is a deep copy of `sl`. It has a different underlying array but contains the same elements.

### Reference to a Slice

- **Definition**: A reference to a slice is essentially a pointer to the slice variable itself, not just the underlying array.
- **Characteristics**:
  - The reference is independent of the underlying array's reallocation.
  - Changes to the slice (like re-slicing or appending) that affect the slice header will be reflected in the referenced slice.

#### Example of Slice Reference

```go
slRef := &sl
```

Here, `slRef` is a reference to `sl`. It points to the slice variable `sl`, not directly to the array.

## Practical Examples

### Mutating Original Slice Without Reallocation

When you modify `sl` without causing a reallocation (i.e., staying within its capacity), both `slShallowCopy` and `*slRef` reflect these changes because they share the same underlying array or slice header.

```go
// Original slice modified
sl[0] = 1
sl[1] = 2
sl[2] = 3
```

### Mutating Original Slice With Reallocation

When `sl` is reallocated (e.g., via `append` that exceeds its capacity), `slShallowCopy` does not reflect these changes, as it still points to the old array. However, `*slRef` still reflects the changes, as it points to the slice variable `sl` itself.

```go
// Original slice reallocated
sl = append(sl, 4)
```

### Mutating Shallow Copy

Modifying `slShallowCopy` affects `sl` until `sl` is reallocated. After reallocation, they become independent.

```go
// Shallow copy modified
slShallowCopy[0] = 10
```

## Conclusion

Understanding the distinctions between shallow copies, deep copies, and references to slices in Go is crucial. Shallow copies share the same underlying array, deep copies create a new array, and references point to the slice variable itself. This knowledge is fundamental for effective data manipulation and management in Go programming.