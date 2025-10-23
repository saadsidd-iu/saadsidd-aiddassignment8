# Testing Guide for Saad Siddique Portfolio Website

This document explains how to run tests for the Flask portfolio website and what each test file covers.

## Test Files Overview

### 1. `test_database.py`
**Purpose**: Tests database functionality and data operations
**Coverage**:
- Database connection and initialization
- CRUD operations (Create, Read, Update, Delete)
- Data integrity and constraints
- Error handling

**Key Tests**:
- `test_database_connection()` - Verifies database connectivity
- `test_add_project()` - Tests project creation
- `test_get_all_projects()` - Tests project retrieval
- `test_update_project()` - Tests project updates
- `test_delete_project()` - Tests project deletion

### 2. `test_app.py`
**Purpose**: Tests Flask application routes and web interface
**Coverage**:
- All website pages (Home, About, Projects, Resume, Contact)
- Form submissions and validation
- Static file serving
- Error handling (404s, form validation)

**Key Tests**:
- `test_home_page()` - Verifies home page loads
- `test_contact_form_submission()` - Tests contact form
- `test_add_project_form_submission()` - Tests project addition form
- `test_static_files()` - Tests CSS and static assets

### 3. `test_integration.py`
**Purpose**: End-to-end integration tests
**Coverage**:
- Complete user workflows
- Cross-component functionality
- Performance and accessibility
- Data persistence across requests

**Key Tests**:
- `test_complete_user_journey()` - Full website navigation
- `test_project_management_workflow()` - Complete project lifecycle
- `test_contact_form_workflow()` - Contact form process
- `test_database_persistence()` - Data persistence verification

## Running Tests

### Prerequisites
Install test dependencies:
```bash
pip install -r test_requirements.txt
```

### Running All Tests
```bash
python run_tests.py
```

### Running Specific Test Files
```bash
# Database tests only
python -m pytest test_database.py -v

# Application tests only
python -m pytest test_app.py -v

# Integration tests only
python -m pytest test_integration.py -v
```

### Running with Coverage
```bash
python -m pytest --cov=. --cov-report=html
```

### Running Individual Tests
```bash
# Run a specific test
python -m pytest test_database.py::TestDatabase::test_database_connection -v

# Run tests matching a pattern
python -m pytest -k "test_database" -v
```

## GitHub Actions

The project includes a GitHub Actions workflow (`.github/workflows/test.yml`) that automatically runs tests on:
- Push to main/develop branches
- Pull requests to main branch
- Multiple Python versions (3.9, 3.10, 3.11)

### Workflow Features
- ✅ Multi-version Python testing
- ✅ Test coverage reporting
- ✅ HTML test reports
- ✅ Codecov integration
- ✅ Artifact uploads

## Test Configuration

### `pytest.ini`
Contains pytest configuration:
- Test discovery patterns
- Output formatting
- Markers for test categorization
- Performance settings

### `test_requirements.txt`
Contains testing-specific dependencies:
- `pytest` - Testing framework
- `pytest-cov` - Coverage reporting
- `pytest-html` - HTML reports
- `pytest-xdist` - Parallel testing

## Test Data

Tests use temporary databases and isolated environments to ensure:
- ✅ No interference with production data
- ✅ Clean test state for each test
- ✅ Parallel test execution
- ✅ Easy cleanup

## Continuous Integration

The GitHub Actions workflow will:
1. **Install Dependencies**: Python + project requirements
2. **Run Database Tests**: Verify data operations
3. **Run Application Tests**: Verify web interface
4. **Run Integration Tests**: Verify end-to-end functionality
5. **Generate Coverage Report**: Code coverage analysis
6. **Upload Results**: Test reports and coverage data

## Troubleshooting

### Common Issues

**Import Errors**:
- Ensure you're in the project root directory
- Check that all dependencies are installed

**Database Errors**:
- Tests use temporary databases, no setup required
- Check that SQLite is available

**Flask App Errors**:
- Tests configure the app for testing automatically
- CSRF is disabled for form testing

### Getting Help

If tests fail:
1. Check the error output for specific issues
2. Run individual tests to isolate problems
3. Check that all dependencies are installed
4. Ensure you're in the correct directory

## Test Coverage Goals

- **Database Operations**: 100% coverage
- **Flask Routes**: 95%+ coverage
- **Form Handling**: 90%+ coverage
- **Error Handling**: 80%+ coverage

## Adding New Tests

When adding new features:
1. Add unit tests to `test_database.py` for data operations
2. Add web tests to `test_app.py` for new routes/forms
3. Add integration tests to `test_integration.py` for workflows
4. Update this documentation if needed

## Best Practices

- ✅ Use descriptive test names
- ✅ Test both success and failure cases
- ✅ Keep tests independent and isolated
- ✅ Use meaningful assertions
- ✅ Clean up test data
- ✅ Document complex test scenarios
