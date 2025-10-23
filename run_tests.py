#!/usr/bin/env python3
"""
Test runner script for the Flask portfolio website
Run this script to execute all tests locally
"""

import subprocess
import sys
import os


def run_command(command, description):
    """Run a command and return success status"""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Command: {command}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print("SUCCESS")
        if result.stdout:
            print("Output:")
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("FAILED")
        print(f"Error: {e}")
        if e.stdout:
            print("Output:")
            print(e.stdout)
        if e.stderr:
            print("Error output:")
            print(e.stderr)
        return False


def main():
    """Main test runner function"""
    print("Flask Portfolio Website - Test Runner")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not os.path.exists('app.py'):
        print("Error: app.py not found. Please run this script from the project root directory.")
        sys.exit(1)
    
    # Check if pytest is installed
    try:
        subprocess.run(['python', '-m', 'pytest', '--version'], 
                      check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("Error: pytest not installed. Please install test requirements:")
        print("pip install -r test_requirements.txt")
        sys.exit(1)
    
    # Run tests
    tests_passed = 0
    total_tests = 0
    
    test_commands = [
        ("python -m pytest test_database.py -v", "Database Tests"),
        ("python -m pytest test_app.py -v", "Application Tests"),
        ("python -m pytest test_integration.py -v", "Integration Tests"),
        ("python -m pytest --cov=. --cov-report=term-missing", "Coverage Report"),
    ]
    
    for command, description in test_commands:
        total_tests += 1
        if run_command(command, description):
            tests_passed += 1
    
    # Summary
    print(f"\n{'='*60}")
    print("TEST SUMMARY")
    print(f"{'='*60}")
    print(f"Tests passed: {tests_passed}/{total_tests}")
    
    if tests_passed == total_tests:
        print("All tests passed!")
        return 0
    else:
        print("Some tests failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
