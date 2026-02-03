import numpy as np
import sympy as sp

# Define two polynomials as lists of coefficients (from lowest to highest degree)
poly1 = [1, 2, 3]  # 1 + 2x + 3x^2
poly2 = [4, 5]     # 4 + 5x

print("Polynomial 1:", poly1)
print("Polynomial 2:", poly2)

def add_polynomials_manual(p1, p2):
    # Make sure p1 is the longer one
    if len(p1) < len(p2):
        p1, p2 = p2, p1
    result = p1[:]
    for i in range(len(p2)):
        result[i] += p2[i]
    return result

manual_sum = add_polynomials_manual(poly1, poly2)
print("Manual sum:", manual_sum)

library_sum = np.polyadd(poly1[::-1], poly2[::-1])[::-1]
print("Library sum:", library_sum)

print("Are they equal?", np.array_equal(manual_sum, library_sum))
if np.array_equal(manual_sum, library_sum):
    print("Yes, the results are the same.")
else:
    print("No, the results differ.")

x = sp.symbols('x')
a, b, c, d, e = sp.symbols('a b c d e')

poly1_sym = [a, b, c]  # a + b x + c x^2
poly2_sym = [d, e]     # d + e x

print("Polynomial 1 symbolic:", poly1_sym)
print("Polynomial 2 symbolic:", poly2_sym)

manual_sum_sym = add_polynomials_manual(poly1_sym, poly2_sym)
print("Manual sum symbolic:", manual_sum_sym)

p1 = sp.Poly(poly1_sym[::-1], x)
p2 = sp.Poly(poly2_sym[::-1], x)
library_sum_sym_poly = p1 + p2
library_sum_sym = library_sum_sym_poly.all_coeffs()[::-1]
print("Library sum symbolic:", library_sum_sym)

print("Manual sum symbolic:", manual_sum_sym)
print("Library sum symbolic:", library_sum_sym)
# Since they are lists of sympy expressions, check if equal
are_equal_sym = manual_sum_sym == library_sum_sym
print("Are they equal?", are_equal_sym)
if are_equal_sym:
    print("Yes, the results are the same for symbolic coefficients.")
else:
    print("No, the results differ for symbolic coefficients.")