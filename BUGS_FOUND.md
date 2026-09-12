# Defects Found & Logged

SauceDemo intentionally seeds a few bugs via special usernames, useful for practicing
defect identification and reporting.

---

**BUG-01: Broken product images for `problem_user`**
- **Severity:** Medium
- **Steps to reproduce:**
  1. Log in as `problem_user` / `secret_sauce`
  2. Observe the product images on the inventory page
- **Expected:** Each product shows its correct image
- **Actual:** All product images show the same broken/wrong image (a dog photo)
- **Status:** Known/seeded defect — used here to demonstrate defect logging workflow

---

**BUG-02: UI lag / performance issue for `performance_glitch_user`**
- **Severity:** Low
- **Steps to reproduce:**
  1. Log in as `performance_glitch_user` / `secret_sauce`
  2. Note load time compared to `standard_user`
- **Expected:** Page loads within ~1–2 seconds like the standard user
- **Actual:** Noticeable multi-second delay on login and page transitions
- **Status:** Known/seeded defect — used to demonstrate non-functional/performance
  observation during functional testing

---

*In a real defect-tracking tool (Jira, Azure DevOps, etc.), each of these would be logged
with environment details, screenshots, and a severity/priority matrix.*
