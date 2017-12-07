
class TestAccess:
    _semiprivate = "variable with semi-private"
    __superprivate = "variable with super-private"

ta = TestAccess()

# PRINT: "variable with semi-private"
print(ta._semiprivate)

# ERROR: AttributeError: 'TestAccess' object has no attribute '__superprivate'
print(ta.__superprivate)
