"""
===============================================================================
Project Title : Aircraft Performance Calculator
File Name     : aircraft_performance.py
Author        : Mohd Tufaiz Ansari
Language      : Python 3
Version       : 1.0

Description:
A menu-driven Python application for calculating fundamental aircraft
performance parameters using standard aerospace engineering equations.

Parameters Included:
- Lift Force
- Drag Force
- Stall Speed
- Lift-to-Drag Ratio
- Dynamic Pressure
- Mach Number
- Rate of Climb
- Wing Loading
- Power Loading
- Range (Breguet Equation)
- Endurance (Breguet Equation)

===============================================================================
"""

import math

g = 9.81


def lift():
    rho = float(input("Air Density (kg/m³): "))
    V = float(input("Velocity (m/s): "))
    S = float(input("Wing Area (m²): "))
    CL = float(input("Lift Coefficient (CL): "))

    L = 0.5 * rho * V**2 * S * CL
    print(f"\nLift Force = {L:.2f} N")


def drag():
    rho = float(input("Air Density (kg/m³): "))
    V = float(input("Velocity (m/s): "))
    S = float(input("Wing Area (m²): "))
    CD = float(input("Drag Coefficient (CD): "))

    D = 0.5 * rho * V**2 * S * CD
    print(f"\nDrag Force = {D:.2f} N")


def stall_speed():
    W = float(input("Aircraft Weight (N): "))
    rho = float(input("Air Density (kg/m³): "))
    S = float(input("Wing Area (m²): "))
    CLmax = float(input("Maximum Lift Coefficient (CLmax): "))

    Vs = math.sqrt((2 * W) / (rho * S * CLmax))
    print(f"\nStall Speed = {Vs:.2f} m/s")


def lift_drag_ratio():
    CL = float(input("Lift Coefficient (CL): "))
    CD = float(input("Drag Coefficient (CD): "))

    LD = CL / CD
    print(f"\nLift-to-Drag Ratio = {LD:.2f}")


def dynamic_pressure():
    rho = float(input("Air Density (kg/m³): "))
    V = float(input("Velocity (m/s): "))

    q = 0.5 * rho * V**2
    print(f"\nDynamic Pressure = {q:.2f} Pa")


def mach_number():
    V = float(input("Aircraft Velocity (m/s): "))
    a = float(input("Speed of Sound (m/s): "))

    M = V / a
    print(f"\nMach Number = {M:.3f}")


def rate_of_climb():
    power_available = float(input("Power Available (W): "))
    power_required = float(input("Power Required (W): "))
    weight = float(input("Aircraft Weight (N): "))

    roc = (power_available - power_required) / weight
    print(f"\nRate of Climb = {roc:.2f} m/s")


def wing_loading():
    weight = float(input("Aircraft Weight (N): "))
    area = float(input("Wing Area (m²): "))

    WL = weight / area
    print(f"\nWing Loading = {WL:.2f} N/m²")


def power_loading():
    weight = float(input("Aircraft Weight (N): "))
    power = float(input("Engine Power (W): "))

    PL = weight / power
    print(f"\nPower Loading = {PL:.6f} N/W")


def range_calculation():
    velocity = float(input("Cruise Velocity (m/s): "))
    sfc = float(input("Specific Fuel Consumption (1/s): "))
    LD = float(input("Lift-to-Drag Ratio: "))
    Wi = float(input("Initial Weight (N): "))
    Wf = float(input("Final Weight (N): "))

    R = (velocity / sfc) * LD * math.log(Wi / Wf)

    print(f"\nEstimated Range = {R:.2f} m")


def endurance():
    sfc = float(input("Specific Fuel Consumption (1/s): "))
    LD = float(input("Lift-to-Drag Ratio: "))
    Wi = float(input("Initial Weight (N): "))
    Wf = float(input("Final Weight (N): "))

    E = (1 / sfc) * LD * math.log(Wi / Wf)

    print(f"\nEstimated Endurance = {E:.2f} seconds")


while True:

    print("\n===================================================")
    print("        AIRCRAFT PERFORMANCE CALCULATOR")
    print("===================================================")

    print("1. Lift Force")
    print("2. Drag Force")
    print("3. Stall Speed")
    print("4. Lift-to-Drag Ratio")
    print("5. Dynamic Pressure")
    print("6. Mach Number")
    print("7. Rate of Climb")
    print("8. Wing Loading")
    print("9. Power Loading")
    print("10. Range")
    print("11. Endurance")
    print("12. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        lift()

    elif choice == "2":
        drag()

    elif choice == "3":
        stall_speed()

    elif choice == "4":
        lift_drag_ratio()

    elif choice == "5":
        dynamic_pressure()

    elif choice == "6":
        mach_number()

    elif choice == "7":
        rate_of_climb()

    elif choice == "8":
        wing_loading()

    elif choice == "9":
        power_loading()

    elif choice == "10":
        range_calculation()

    elif choice == "11":
        endurance()

    elif choice == "12":
        print("\nThank you for using the Aircraft Performance Calculator.")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1 and 12.")
