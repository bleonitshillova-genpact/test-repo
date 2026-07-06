#!/usr/bin/env python3
"""
Python Test Script - Testing Environment Activity
Demonstrates basic Python execution and validation
"""

import sys
import json
from datetime import datetime


def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}! Welcome to the testing environment."


def calculate_sum(numbers):
    """Calculate sum of a list of numbers"""
    return sum(numbers)


def get_system_info():
    """Get basic system information"""
    return {
        "python_version": sys.version,
        "timestamp": datetime.now().isoformat(),
        "platform": sys.platform
    }


def main():
    print("=" * 50)
    print("Python Test Script Execution")
    print("=" * 50)

    # Test 1: Greeting
    print("\n[Test 1] Greeting Function:")
    print(greet("Tester"))

    # Test 2: Calculation
    print("\n[Test 2] Sum Calculation:")
    numbers = [10, 20, 30, 40, 50]
    result = calculate_sum(numbers)
    print(f"Sum of {numbers} = {result}")

    # Test 3: System Info
    print("\n[Test 3] System Information:")
    info = get_system_info()
    print(json.dumps(info, indent=2))

    print("\n" + "=" * 50)
    print("[OK] All tests completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
