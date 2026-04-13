# Software Requirements Specification (SRS)

## Requirement Review and सुधार

---

### 1. Requirement:
"The system should be user-friendly."

Problems:
- Not clear ❌
- Not measurable ❌
- Not testable ❌
- Ambiguous ❌

Improved Requirement:
The system shall provide a graphical user interface where a new user can complete registration within 2 minutes without external help.

---

### 2. Requirement:
"The system shall store student records safely."

Problems:
- Not specific ❌
- Not testable ❌
- Ambiguous ❌

Improved Requirement:
The system shall store student records in an encrypted database using AES-256 encryption and restrict access to authorized users only.

---

### 3. Requirement:
"The system should load quickly."

Problems:
- Not measurable ❌
- Not clear ❌
- Not testable ❌

Improved Requirement:
The system shall load the homepage within 2 seconds for 95% of users under normal network conditions.

---

### 4. Requirement:
"The system shall allow users to register, login, and manage their profile."

Problems:
- Not atomic ❌ (multiple functions in one)
- Not fully detailed ❌

Improved Requirements:

a) The system shall allow users to register using email and password.

b) The system shall allow registered users to log in using valid credentials.

c) The system shall allow users to update their profile information including name and password.

---

### 5. Requirement:
"The system shall send notifications."

Problems:
- Not specific ❌
- Not clear ❌
- Not testable ❌

Improved Requirement:
The system shall send email notifications to users within 5 seconds after successful registration or password change.

---
