# Week 2 Tutorial: Movie Theater Admission Logic

### 1. Identify the Components
* **1.1. Inputs:** * Age (Integer)
  * Accompanied by an adult (Boolean: True/False)
  * Has a valid ticket (Boolean: True/False)
* **1.2. Process:** Check if the person is at least 13 OR accompanied by an adult, AND also ensure they have a valid ticket.
* **1.3. Output:** "Access Allowed" or "Access Denied"

### 2. Design the Algorithm
* **2.2. Truth Table:** Let A = Age >= 13, B = Accompanied, C = Has Ticket

| Age >= 13 (A) | Accompanied (B) | Has Ticket (C) | Output (Allowed?) |
| :--- | :--- | :--- | :--- |
| False | False | False | False |
| False | False | True | False |
| False | True | False | False |
| False | True | True | True |
| True | False | False | False |
| True | False | True | True |
| True | True | False | False |
| True | True | True | True |


![alt text](image-1.png)
* **2.3. Step-by-Step Solution:**
  1. Ask the user for their age.
  2. Ask the user if they are accompanied by an adult (yes/no).
  3. Ask the user if they have a valid ticket (yes/no).
  4. Evaluate the rule: If (Age >= 13 OR Accompanied is True) AND Has Ticket is True.
  5. If the conditions are met, output "Access Allowed". Otherwise, output "Access Denied".

* **2.4.Pseudocode:**
```text
BEGIN
    INPUT age
    INPUT is_accompanied
    INPUT has_ticket

    IF (age >= 13 OR is_accompanied == True) AND has_ticket == True THEN
        OUTPUT "Access Allowed"
    ELSE
        OUTPUT "Access Denied"
    ENDIF
END

* **2.3. Step-by-Step Solution:**
  1. Ask for user's age.
  2. Ask if accompanied by an adult.
  3. Ask if they have a ticket.
  4. Evaluate rules: (Age >= 13 OR Accompanied) AND Ticket == True.
  5. Print result.