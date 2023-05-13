#### Taichi

This is a cheat sheet for the Taichi framework.

> Taichi is embedded in Python and uses modern just-in-time (JIT) frameworks (for example LLVM, SPIR-V) to offload the Python source code to native GPU or CPU instructions, offering the performance at both development time and runtime.
>
> See the original documentation [here](https://docs.taichi-lang.org/docs/overview).

To use Taichi, with CUDA backend, in Python:

```python
import taichi as ti
ti.init(arch=ti.cuda)
```

##### Type system

The `ti.types` module in Taichi defines all of the supported data types. These data types are categorized into two groups: primitive and compound.

- Primitive types encompass commonly utilized numerical data types, such as `ti.i32` (`int32`), `ti.u8` (`uint8`), and `ti.f64` (`float64`).
- Compound types, on the other hand, encompass array-like or struct-like data types, including `ti.types.matrix`, `ti.types.ndarray`, and `ti.types.struct`. These types are composed of multiple members, which can be primitive or other compound types.

Type is assigned to variables on definition.

Type casting for scalars can be done with `ti.cast(x, ti.f32)` or `ti.f32(x)`. For compound types, only `ti.vector` and `ti.matrix` support element-wise casting.

##### Containers

**Containers** organize multiple elements of various **data types**. There are two types of containers: `field` and `ndarray`.

- `field` might have very complicated tree-structured layouts with even sparsity in them. It is hard for external libraries to interpret or use computed results stored in `ti.field` directly.
- An `ndarray`, always allocates a contiguous memory block to allow straightforward data exchange with external libraries.

A container should be constructed in the Python scope:

```python
f = ti.field(ti.f32, shape=(3, 2))
a = ti.ndarray(ti.f32, shape=())
# Access the value using tuple:
f[1, 2]
```

- Taichi does not support slicing in containers.
- `f.fill(val)` resets the value, and it works in both scopes.
- `a.copy_from(b)` copies data between containers. Both `copy.copy` and `copy.deepcopy` are supported.
- Accessing elements of a container in Python scople launches a small Taichi kernel. For efficiency, use `d.to_torch(device="cuda")` and `d.from_torch(e)` to convert to and from Torch tensors. Taichi will maintain a separate copy, rather than keep a reference.

##### `ndarray` arguments

`ndarray` can be used as kernel arguments, this has a different semantic than using it as a container. The kernel can accept NumPy and PyTorch tensors as arguments now.

```python
@ti.kernel
def foo(A: ti.types.ndarray(dtype=ti.f32, ndim=2)):
    do_something()
```

- We need to specify `ndim` instead of `shape` when using `ndarray` as argument. We can also rely on runtime inference of `dtype` and `ndim` by writing `A: ti.types.ndarray()`.
- When the data type and device match the argument type, no copy will happen. Otherwise implicit transfer happens.
- Only continuous NumPy arrays and PyTorch tensors are supported.

##### Kernels and Functions

Functions decorated with `@ti.kernel` are known as **Taichi kernels**.

- Entry points to the **Taichi scope**, must be invoked by Python code.
- Must be type annotated, unless no return or no arguments. Only accepts restricted types.
- Kernels are compiled when first called. All global variables are treated as constants.
- There can only be one return value and at most one return statement.

Functions decorated with `@ti.func` are known as **Taichi functions**.

- Must not be invoked within Taichi scope.
- Runtime recursion is not allowed.
- There can be multiple return values, but at most one return statement.

##### Parallel `for` Loop

```python
for_stmt        ::= "for" target_list "in" iter_expression ":" suite
iter_expression ::= static_expression | expression
```

- The `for` loops can iterate in parallel if they are in the **outermost scope**.
- You can write `ti.loop_config(serialize=True)` before a range/ndrange `for` loop to let it run serially, then it can be terminated by `break` statements.

The range `for` statement iterates over a range of numbers.

```python
for i in range(10):
```

- The `iter_expression` of range `for` statement must be like `range(start, stop)` or `range(stop)`.

The `ndrange for` iterates over multidimensional ranges.

```python
for i, j in ti.ndrange(10, 2):
```

- The `iter_expression` of `ndrange for` statement must be a call to `ti.ndrange()` or a nested call to `ti.grouped(ti.ndrange())`.

  - If the `iter_expression` is a call to `ti.range()`, it is a normal ndrange `for`.

  - If the `iter_expression` is a call to `ti.grouped(ti.range())`, it is a grouped ndrange `for`.

- `ti.ndrange` receives arbitrary numbers of arguments. The k-th argument represents the iteration range of the k-th dimension.

The `struct for` statement iterates over every active elements in a Taichi field.

```python
for i, j in field:
```

- If the `iter_expression` is a Taichi field, it is a normal struct `for`.
- If the `iter_expression` is a call to `ti.grouped(x)` where `x` is a Taichi field, it is a grouped struct `for`.

The static `for` statement unrolls a range/ndrange `for` loop at compile time.

```python
for i in ti.static(range(5)):
```

Grouped for works as the following:

```python
@ti.kernel
def copy_1D(x: ti.template(), y: ti.template()):
    for i in x:
        y[i] = x[i]

@ti.kernel
def copy_2d(x: ti.template(), y: ti.template()):
    for i, j in x:
        y[i, j] = x[i, j]

# Kernels listed above can be unified into one kernel using `ti.grouped`:
@ti.kernel
def copy(x: ti.template(), y: ti.template()):
    for I in ti.grouped(y):
        # I is a vector with dimensionality same to y
        # If y is 0D, then I = ti.Vector([]), which is equivalent to `None` used in x[I]
        # If y is 1D, then I = ti.Vector([i])
        # If y is 2D, then I = ti.Vector([i, j])
        # ...
        x[I] = y[I]
```


