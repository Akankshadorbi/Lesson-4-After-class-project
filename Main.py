# ============================================================
#classroom points
# ============================================================

# --- Assignment Operator (=) ---
# Store the harvest in kg from each of the 5 fields
math = 115
science = 60
english = 75
history = 95
geography = 120

# --- Arithmetic Operators (+, -, *, /) ---
# Calculate total and average harvest
total   = math + science + english + history + geography
average = total / 5

print("Total points     :", total, "points")
print("Average per field  :", average, "points")

# Points per class is 15 — calculate total earnings
points_per_class = 15
earnings = total * points_per_class
print("Total earnings     : points.", earnings)

# --- Floor Division (//) and Modulus (%) ---
# Pack the harvest into bags of 25 kg each
points    = total // 30
leftover = total % 20

print("points per class   :", points, "points")
print("Leftover points     :", leftover, "points")

# --- Comparison Operators (>, <, ==, >=) ---
# Compare this year's harvest with last year
last_year = 600
print("Better than last year?  :", total > last_year)
print("Same as last year?      :", total == last_year)
print("At least as good?       :", total >= last_year)

# --- Assignment Operators (+=, -=) ---
# A bonus field adds 30 kg to the total
total += 30
print("After bonus points :", total, "points")

# Subtract 15 kg saved as seeds for next season
total -= 30
print("After seed reserve :", total, "points")

# Final bag count after all adjustments
points = total // 25
print("points  :", points)

