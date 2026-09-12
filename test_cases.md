# Test Case Design — SauceDemo

Documented before automation, as part of STLC test design.

## Module: Login

| ID | Title | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-01 | Valid login | Enter `standard_user` / `secret_sauce`, click Login | Redirected to inventory page | High |
| TC-02 | Invalid password | Enter `standard_user` / `wrong_pass`, click Login | Error: "Username and password do not match" | High |
| TC-03 | Empty credentials | Leave both fields blank, click Login | Error: "Username is required" | Medium |
| TC-04 | Locked-out user | Enter `locked_out_user` / `secret_sauce`, click Login | Error: "user has been locked out" | High |

## Module: Inventory / Product Sorting

| ID | Title | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-05 | Sort price low→high | Select "Price (low to high)" from dropdown | Products reordered ascending by price | Medium |
| TC-06 | Sort name Z→A | Select "Name (Z to A)" from dropdown | Products reordered descending alphabetically | Low |
| TC-07 | Add single item to cart | Click "Add to cart" on one product | Cart badge shows "1"; button changes to "Remove" | High |
| TC-08 | Add multiple items to cart | Add 3 different products | Cart badge shows "3" | High |

## Module: Checkout

| ID | Title | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-09 | Complete checkout — happy path | Add item → cart → checkout → fill info → finish | "Thank you for your order" confirmation shown | High |
| TC-10 | Checkout with missing postal code | Fill first/last name only, leave postal blank | Error: "Postal Code is required" | Medium |

## Module: API (sample, against a public REST API)

| ID | Title | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-11 | GET single user returns 200 | GET `/api/users/2` | Status 200, response contains user `id` | High |
| TC-12 | GET non-existent user returns 404 | GET `/api/users/9999` | Status 404 | Medium |
