# Complete Testing Guide

This guide walks through all testing activities for the environment setup.

## 1. Git Operations Testing

### Test git status and branch operations
```bash
# Check current status
git status

# Create a new branch
git checkout -b test-branch

# Make a change
echo "Test content" > git-test.txt
git add git-test.txt
git commit -m "Test: Add git test file"

# Push to remote
git push -u origin test-branch

# Switch back to main
git checkout main

# View branches
git branch -a
```

### Test git clone (in a different directory)
```bash
cd ..
git clone https://github.com/bleonitshillova-genpact/test-repo.git test-repo-clone
cd test-repo-clone
```

---

## 2. Python Code Execution

### Run the main test script
```bash
cd python-tests
python test_script.py
```

Expected output:
- Greeting function test
- Sum calculation test
- System information display

### Run the database test
```bash
python database_test.py
```

Expected output:
- Creates `test_database.db`
- Inserts sample data
- Queries and displays records
- Shows DBeaver connection instructions

---

## 3. Database Connectivity (DBeaver)

### Steps to test in DBeaver:

1. **Open DBeaver**

2. **Create New Connection:**
   - Click "Database" → "New Database Connection"
   - Select "SQLite"
   - Click "Next"

3. **Configure Connection:**
   - Path: Browse to `c:\Users\602000837\Desktop\test-repo\python-tests\test_database.db`
   - Click "Test Connection"
   - Click "Finish"

4. **Test Queries:**
   ```sql
   -- View all users
   SELECT * FROM test_users;
   
   -- Count records
   SELECT COUNT(*) FROM test_users;
   
   -- Filter by username
   SELECT * FROM test_users WHERE username = 'alice';
   ```

---

## 4. Frontend Application Testing

### Start a local web server
```bash
cd frontend

# Option 1: Using Python
python -m http.server 3000

# Option 2: Using Node.js (if installed)
# npx serve -p 3000
```

### Test in Browser:
1. Open: `http://localhost:3000`
2. Test the greeting function (enter name and click button)
3. Test API connectivity (click API test button)
4. Load test data (click load data button)
5. Verify all status indicators show "Active"

---

## 5. API Testing

### Start the API server
```bash
cd api-server
python server.py
```

The server will start on `http://localhost:8000`

### Manual API Testing (using curl or browser):

```bash
# Health check
curl http://localhost:8000/health

# Get all users
curl http://localhost:8000/users

# Get specific user
curl http://localhost:8000/users?id=1

# Create new user (POST)
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Diana","email":"diana@example.com","role":"User"}'

# Get status
curl http://localhost:8000/status
```

---

## 6. Postman API Testing

### Import Collection into Postman:

1. **Open Postman**

2. **Import Collection:**
   - Click "Import" button
   - Select "File"
   - Browse to: `api-server/postman_collection.json`
   - Click "Import"

3. **Run Tests:**
   - Make sure the API server is running (`python server.py`)
   - Click on each request in the collection
   - Click "Send" button
   - Verify the response

4. **Test All Endpoints:**
   - Health Check → Should return status "healthy"
   - Get All Users → Should return 3 users
   - Get User by ID → Should return specific user
   - Create User → Should return 201 status
   - Get Status → Should return server info

---

## Complete Testing Checklist

- [ ] **Git Operations**
  - [ ] git clone works
  - [ ] git status shows correct state
  - [ ] git branch creation works
  - [ ] git commit works
  - [ ] git push to remote works

- [ ] **Python Execution**
  - [ ] test_script.py runs successfully
  - [ ] All functions execute without errors
  - [ ] Output is displayed correctly

- [ ] **Database Testing**
  - [ ] database_test.py creates database
  - [ ] Sample data is inserted
  - [ ] Queries return correct results
  - [ ] DBeaver can connect to database
  - [ ] SQL queries work in DBeaver

- [ ] **Frontend Testing**
  - [ ] Web server starts successfully
  - [ ] Page loads in browser
  - [ ] Greeting function works
  - [ ] API test button responds
  - [ ] Data loading works
  - [ ] All styles are applied correctly

- [ ] **API Server Testing**
  - [ ] Server starts on port 8000
  - [ ] All endpoints respond
  - [ ] GET requests return data
  - [ ] POST requests create resources
  - [ ] CORS headers are present

- [ ] **Postman Testing**
  - [ ] Collection imports successfully
  - [ ] All 5 requests work
  - [ ] Response status codes are correct
  - [ ] Response data is valid JSON
  - [ ] POST request creates new user

---

## Troubleshooting

### Port Already in Use
If ports 3000 or 8000 are in use, modify the port numbers:
- Frontend: Use different port with `python -m http.server 3001`
- API: Edit `server.py` and change port number

### Python Not Found
Ensure Python is installed and in PATH:
```bash
python --version
# or
python3 --version
```

### Database Permission Issues
Ensure write permissions in the `python-tests` directory

### CORS Errors
The API server includes CORS headers. If issues persist, check browser console for details.

---

## Summary

This testing environment covers:
1. ✓ Git operations (clone, push, commit, branch)
2. ✓ Code generation by Claude (all files created)
3. ✓ Python code execution (2 test scripts)
4. ✓ Frontend application (HTML/CSS/JS)
5. ✓ Database connectivity (SQLite + DBeaver)
6. ✓ API testing (REST server + Postman collection)

All components are ready for testing!
