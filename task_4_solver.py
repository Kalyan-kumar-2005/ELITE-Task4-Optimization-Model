#include <stdio.h>

long long min(long long a, long long b) {
    return a < b ? a : b;
}

long long taumBday(long long b, long long w, long long bc, long long wc, long long z) {
    
}

int main() {
    int t;
    scanf("%d", &t);

    while (t--) {
        long long b, w, bc, wc, z;

        scanf("%lld %lld", &b, &w);
        scanf("%lld %lld %lld", &bc, &wc, &z);

        long long result = taumBday(b, w, bc, wc, z);
        printf("%lld\n", result);
    }

    return 0;
}

# task_4_solver.py

# --- TASK 4: OPTIMIZATION MODEL (Linear Programming) ---

# Import the Pulp library
from pulp import *

# 1. Define the Problem
prob = LpProblem("Resource_Allocation_Profit_Maximization", LpMaximize)

# 2. Define Decision Variables
# x1 = Number of units of Toy A
# x2 = Number of units of Toy B
x1 = LpVariable("Toy_A_Units", lowBound=0, cat='Integer')
x2 = LpVariable("Toy_B_Units", lowBound=0, cat='Integer')

# 3. Objective Function (Maximize Profit)
# Profit = ($4 * x1) + ($5 * x2)
prob += 4 * x1 + 5 * x2, "Total_Profit"

# 4. Constraints (Machine Time Limits)
# Constraint 1: Machine 1 time limit (Max 20 hours)
prob += 1 * x1 + 2 * x2 <= 20, "Machine_1_Time"

# Constraint 2: Machine 2 time limit (Max 15 hours)
prob += 3 * x1 + 1 * x2 <= 15, "Machine_2_Time"

# 5. Solve the Optimization Problem
prob.solve()

# 6. Extract Solution and Insights
print("\n--- SOLUTION AND INSIGHTS (Task 4 Deliverable) ---")
print(f"Solution Status: {LpStatus[prob.status]}")

if LpStatus[prob.status] == "Optimal":
    production_a = value(x1)
    production_b = value(x2)
    max_profit = value(prob.objective)

    print("\n--- Optimal Production Plan Found ---")
    print(f"1. Optimal Production: {production_a} units of Toy A")
    print(f"2. Optimal Production: {production_b} units of Toy B")
    print(f"3. Maximum Possible Profit (Z): ${max_profit:,.2f}")
    
    print("\n--- Constraint Usage ---")
    print(f"Machine 1 Used: {value(1 * x1 + 2 * x2)} hours (Out of 20)")
    print(f"Machine 2 Used: {value(3 * x1 + 1 * x2)} hours (Out of 15)")

else:
    print("Error: Could not find an optimal solution.")