# -----------False------------
# If an object evaluated to 0 is always zero
print(bool(0))
print(bool(0.0))
# Empth list, dict, tuple always zero
print(bool(''))
print(bool([]))
print(bool({}))
# Python None always evaluated to zero
print(bool(None))

# -----------True------------
# All numbers except zero are evaluated to True
print(bool(1))
print(bool(-1))
print(bool(42))
print(bool(0.00000000000001))
# Non-Empth string is evaluated to True
print(bool('India'))
# Non-Empty list, tuple always True
print(bool([42, 43, 44]))
print(bool({'a': 42, 'b': 42}))
