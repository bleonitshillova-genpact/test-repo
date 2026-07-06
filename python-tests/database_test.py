#!/usr/bin/env python3
"""
Database Connectivity Test - DBeaver Compatible
Demonstrates database connection patterns for testing
"""

import sqlite3
from datetime import datetime


def create_test_database(db_path="test_database.db"):
    """Create a test SQLite database"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create test table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Insert sample data
    sample_users = [
        ("alice", "alice@example.com"),
        ("bob", "bob@example.com"),
        ("charlie", "charlie@example.com")
    ]

    cursor.executemany(
        "INSERT INTO test_users (username, email) VALUES (?, ?)",
        sample_users
    )

    conn.commit()
    return conn, cursor


def test_database_queries(cursor):
    """Run test queries"""
    print("\n[Database Test] Querying test_users table:")
    cursor.execute("SELECT * FROM test_users")
    rows = cursor.fetchall()

    print(f"\nFound {len(rows)} users:")
    for row in rows:
        print(f"  ID: {row[0]}, Username: {row[1]}, Email: {row[2]}")

    return rows


def main():
    print("=" * 60)
    print("Database Connectivity Test (DBeaver Compatible)")
    print("=" * 60)

    try:
        # Create and populate database
        print("\n[Step 1] Creating test database...")
        conn, cursor = create_test_database()
        print("[OK] Database created: test_database.db")

        # Run queries
        print("\n[Step 2] Running test queries...")
        rows = test_database_queries(cursor)
        print(f"[OK] Successfully retrieved {len(rows)} records")

        # Connection info for DBeaver
        print("\n" + "=" * 60)
        print("DBeaver Connection Information:")
        print("=" * 60)
        print("Database Type: SQLite")
        print(f"Database File: test_database.db")
        print("Path: c:\\Users\\602000837\\Desktop\\test-repo\\python-tests\\")
        print("\nTo connect in DBeaver:")
        print("1. Create New Database Connection")
        print("2. Select SQLite")
        print("3. Browse to the database file path above")
        print("4. Test Connection")
        print("=" * 60)

        conn.close()
        print("\n[OK] Database test completed successfully!")

    except Exception as e:
        print(f"\n[ERROR] Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
