# SauceDemo Automated Test Suite

A Selenium + Python automated regression suite for [saucedemo.com](https://www.saucedemo.com),
a demo e-commerce site built by Sauce Labs specifically for QA/automation practice.
Uses the **Page Object Model (POM)** design pattern — the same pattern used in real
enterprise automation frameworks.

## What this covers (maps directly to the job requirements)

| JD Requirement | Where it's demonstrated |
|---|---|
| Selenium WebDriver | All tests drive a real browser via Selenium |
| Python programming | Entire suite written in Python |
| Test case design (STLC) | `test_cases.md` — documented scenarios before automation |
| Functional & regression testing | Login, inventory, cart, checkout flows |
| Defect logging | `BUGS_FOUND.md` — real bugs SauceDemo intentionally seeds, logged like a QA would |
| Pytest / test framework | Uses `pytest` as the test runner |
| Git / version control | Structured as a Git-ready repo |
| API testing concepts | `test_api.py` — a small requests-based API test against a public API |

## Project structure

```
qa-project/
├── pages/              # Page Object Model classes
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/
│   ├── test_login.py       # Login: positive + negative cases
│   ├── test_inventory.py   # Sorting, add-to-cart, cart badge count
│   ├── test_checkout.py    # End-to-end checkout flow
│   └── test_api.py         # API testing example (requests library)
├── test_cases.md        # Manual test case design (STLC artifact)
├── BUGS_FOUND.md         # Defects found & logged, with repro steps
├── conftest.py           # Pytest fixtures (browser setup/teardown)
├── requirements.txt
└── README.md
```

## Setup (run this on your own machine — needs internet + Chrome)

```bash
pip install -r requirements.txt
pytest -v                      # run everything
pytest tests/test_login.py -v  # run one file
pytest -m regression -v        # run only regression-tagged tests
```

Selenium 4.6+ auto-manages the ChromeDriver binary — you just need Google Chrome installed.

## Why SauceDemo

It's the industry-standard practice site for QA portfolios: it has known, intentional bugs
(e.g. `problem_user` shows broken product images), multiple user roles to test (locked-out
user, performance-glitch user), and stable selectors — so it's realistic without being
flaky, which is exactly what you want in a portfolio project an interviewer can run themselves.

## Next steps to extend this (good talking points in an interview)

- Add TestNG-style HTML reporting via `pytest-html`
- Wire this into GitHub Actions for CI/CD (ties to the JD's "Jenkins/CI-CD" preferred skill)
- Add a BDD layer with `pytest-bdd` or `behave` (ties to "Cucumber" preferred skill)
- Add data-driven tests (login with multiple username/password pairs from a CSV)
