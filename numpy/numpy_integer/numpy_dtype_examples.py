import numpy as np

# Integer types
int8_arr = np.array([1, 2, 3], dtype=np.int8)
int16_arr = np.array([1000, 2000, 3000], dtype=np.int16)
int32_arr = np.array([100000, 200000, 300000], dtype=np.int32)
int64_arr = np.array([10000000000, 20000000000, 30000000000], dtype=np.int64)

# Unsigned integer types
uint8_arr = np.array([0, 255, 128], dtype=np.uint8)
uint16_arr = np.array([0, 65535, 12345], dtype=np.uint16)
uint32_arr = np.array([0, 4294967295, 1234567890], dtype=np.uint32)
uint64_arr = np.array([0, 18446744073709551615], dtype=np.uint64)

# Floating point types
float16_arr = np.array([1.0, 2.0, 3.0], dtype=np.float16)
float32_arr = np.array([1.5, 2.5, 3.5], dtype=np.float32)
float64_arr = np.array([1.23456789, 2.34567891, 3.45678912], dtype=np.float64)

# Complex number types
complex64_arr = np.array([1 + 2j, 3 + 4j], dtype=np.complex64)
complex128_arr = np.array([1 + 2j, 3 + 4j], dtype=np.complex128)

# Boolean type
bool_arr = np.array([True, False, True], dtype=np.bool_)

# String types
string_arr = np.array(["hello", "numpy"], dtype=np.str_)
bytes_arr = np.array([b"hello", b"world"], dtype=np.bytes_)

# Unicode and fixed-length string types
fixed_string_arr = np.array(["abc", "def"], dtype="U5")
fixed_bytes_arr = np.array([b"abc", b"def"], dtype="S5")

# Object type
obj_arr = np.array([1, "two", 3.0], dtype=object)

# Datetime and timedelta types
datetime_arr = np.array(["2025-01-01", "2025-12-31"], dtype="datetime64[D]")
timedelta_arr = np.array([1, 2, 3], dtype="timedelta64[D]")

# Structured dtype
structured_arr = np.array(
    [(1, 1.5, "Alice"), (2, 2.5, "Bob")],
    dtype=[("id", "i4"), ("score", "f4"), ("name", "U10")],
)

# Views and dtype conversion
cast_float_to_int = float64_arr.astype(np.int32)
cast_int_to_float = int16_arr.astype(np.float64)

# Print dtype examples
examples = [
    ("int8", int8_arr),
    ("int16", int16_arr),
    ("int32", int32_arr),
    ("int64", int64_arr),
    ("uint8", uint8_arr),
    ("uint16", uint16_arr),
    ("uint32", uint32_arr),
    ("uint64", uint64_arr),
    ("float16", float16_arr),
    ("float32", float32_arr),
    ("float64", float64_arr),
    ("complex64", complex64_arr),
    ("complex128", complex128_arr),
    ("bool", bool_arr),
    ("string", string_arr),
    ("bytes", bytes_arr),
    ("fixed_unicode", fixed_string_arr),
    ("fixed_bytes", fixed_bytes_arr),
    ("object", obj_arr),
    ("datetime64[D]", datetime_arr),
    ("timedelta64[D]", timedelta_arr),
    ("structured", structured_arr),
    ("cast float64 -> int32", cast_float_to_int),
    ("cast int16 -> float64", cast_int_to_float),
]

if __name__ == "__main__":
    print("NumPy dtype examples")
    print("====================")
    for name, arr in examples:
        print(f"\n{name} -> dtype: {arr.dtype}")
        print(arr)

    print("\nStructured record access:")
    print(structured_arr[0]["name"], structured_arr[1]["score"])
    print("\nDatetime arithmetic:")
    print(datetime_arr + np.timedelta64(7, "D"))
    print("\nTimedelta sum:")
    print(np.sum(timedelta_arr))
