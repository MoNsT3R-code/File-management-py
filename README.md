# School-management-app

A comprehensive **educational ERP platform** for Al-Noor Islamic Academy with integrated administrative, grading, financial workflows, and specialized Islamic education modules (Hifz & Tarbiyah tracking).

![Python](https://img.shields.io/badge/Backend-Python-blue?logo=python)
![C](https://img.shields.io/badge/Performance-C-black?logo=c)
![SQL](https://img.shields.io/badge/Database-SQL-orange?logo=mysql)
![ERP](https://img.shields.io/badge/Type-ERP%20System-brightgreen)
![Multi-Tenant](https://img.shields.io/badge/Architecture-Multi%20Tenant-blue)
![Cloud](https://img.shields.io/badge/Deployment-Cloud%20Ready-green)
![RBAC](https://img.shields.io/badge/Security-RBAC-red)

---

## Al-Noor Islamic Academy - Student Management Platform

A multi-tenant, cloud-based educational resource planning (ERP) platform designed for Al-Noor Islamic Academy. The system integrates standard school administrative modules with specialized Islamic tracking systems such as Hifz and Tarbiyah logs. It features a decoupled architectural pattern using Python, JavaScript, SQL, HTML, and high-performance native C extensions.

---

## 📍 Quick Navigation

* [🌐 Engine Overview](#-engine-overview)
* [📦 System Architecture](#-system-architecture)
* [✨ Key Features](#-key-features)
* [📁 Repository Structure](#-repository-structure-and-module-index)
* [🛠️ Tech Stack](#️-tech-stack)
* [💻 System Requirements](#-system-requirements)
* [🚀 Deployment and Execution Guide](#-deployment-and-execution-guide)
* [🏗️ Architectural Highlights](#%EF%B8%8F-architectural-highlights)
* [🎯 Islamic Education Features](#-islamic-education-features)
* [📄 License](#-license)

--- 

## 📦 System Architecture

┌─────────────────────────────────────────────────────────────┐
│                       FRONTEND LAYER                        │
├──────────────────────────────┬──────────────────────────────┤
│        frontend.html         │        Management.js         │
│         (UI Layout)          │   (User Experience & API)    │
└──────────────────────────────┴──────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────┐
│                     BACKEND PROCESSING                      │
├────────────┬─────────────┬────────────┬─────────────┬───────┤
│ attendance │ finance.py  │metrices.py │  report.py  │file_io│
│    .py     │ (Billing &  │ (Grading)  │  (Reports)  │_core.c│
│(Attendance)│ Concession) │            │             │(Native)│
└──────────────────────────────┴──────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────┐
│                       DATABASE LAYER                        │
├─────────────────────────────────────────────────────────────┤
│        database.sql (MariaDB 10.5+ / PostgreSQL 14+)        │
│ ┌──────────┬───────────┬───────────┬───────────────┬──────┐ │
│ │   RBAC   │ Academic  │ Financial │ Hifz/Tarbiyah │ Bio  │ │
│ └──────────┴───────────┴───────────┴───────────────┴──────┘ │
└─────────────────────────────────────────────────────────────┘

---

## ✨ Key Features

✅ **Multi-tenant Architecture** - Isolated data per institution  
✅ **Role-Based Access Control (RBAC)** - Admin, Teachers, Students, Parents  
✅ **Biometric Attendance** - Native C integration for fast processing  
✅ **Islamic Curriculum Modules** - Hifz (Quran memorization) & Tarbiyah tracking  
✅ **Financial Management** - Tuition billing, concessions, balance tracking  
✅ **Automated Grading** - Weighted grades from quizzes, assignments, exams  
✅ **Parent-Student Dashboard** - Real-time progress reports  
✅ **Performance Analytics** - Visual charts & insights  

---

## 📁 Repository Structure and Module Index

The project codebase is organized into the following components:

### Frontend and Interface Layers
* **frontend.html** - Structural user interface layout built with HTML and styled via utility frameworks to reflect the institutional identity.
* **Management.js** - Scripting logic for handling the frontend user experience, role validation tracking, and asynchronous client-to-server API updates.

### Core Database Configuration
* **database.sql** - Transactional relational database schema for MariaDB/PostgreSQL. Sets up strict constraints for RBAC, academic course routing, specialized Hifz metrics matrices, and financial ledger data tables.

### Processing Engines and Pipelines
* **file_io_core.c** - Native C extension optimized for performance-critical operations such as biometric attendance stream processing.
* **attendance.py** - Ingestion script managing morning and mid-day prayer attendance using Python's `ctypes` bindings to interface with the compiled C library.
* **finance.py** - Automated billing pipeline that calculates tuition, processes concessions, tracks balances, and records transaction history.
* **metrices.py** - Analytical engine computing weighted student grades from quizzes, assignments, and term examinations.
* **report.py** - Automated document generation converting academic analytics into report cards and visual progress charts.

### Documentation
* **README.md** - This repository guide and technical implementation manual.

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | HTML5, JavaScript (Vanilla) |
| **Backend** | Python 3.8+ |
| **Performance Layer** | C (Native Extensions) |
| **Database** | MariaDB 10.5+ / PostgreSQL 14+ |
| **Architecture** | Multi-tenant ERP |
| **Security** | RBAC, Input Validation |
| **Deployment** | Cloud-ready |

---

## 💻 System Requirements

To deploy and run the modules in this directory, ensure the host environment meets the following baseline configurations:

* **Operating System:** Linux, macOS, or Windows (Linux recommended for C compilation)
* **Database Engine:** MariaDB 10.5+ or PostgreSQL 14+
* **Python Runtime:** Python 3.8+ with standard data analysis libraries
* **C Compiler:** GCC or Clang toolchain
* **Memory:** Minimum 2GB RAM for production deployment
* **Storage:** 500MB+ for database and file storage

---

## 🚀 Deployment and Execution Guide

### Step 1: Database Initialization

Import the database schema into your relational database instance:

```bash
# For MariaDB
mysql -u root -p < database.sql

# For PostgreSQL
psql -U postgres -d school_db -f database.sql

```

### Step 2: Compile Native C Extension
Compile the performance-critical file I/O layer into a shared library:

```bash
# For Linux/macOS
gcc -shared -o file_io_core.so -fPIC file_io_core.c

# For Windows
gcc -shared -o file_io_core.dll file_io_core.c

```

### Step 3: Install Python Dependencies

```bash

pip install -r requirements.txt

```

### Step 4: Execute Core Subsystems
Run specific backend pipelines from your console:

```bash

# Process attendance (morning & mid-day prayer)
python3 attendance.py

# Calculate weighted academic grades
python3 metrices.py

# Process financial billing cycle
python3 finance.py

# Generate student report cards and visualizations
python3 report.py

```

### Step 5: Launch Frontend
Serve the HTML frontend on your local or cloud server:

```bash

# Using Python's built-in server
python3 -m http.server 8000

# Then visit: http://localhost:8000

```

## 🏗️ Architectural Highlights
### 🔀 Decoupled Architecture
Client-side rendering is cleanly separated from backend analytical code, allowing cross-functional operations to execute independently without blocking the UI.

### ⚡ Memory Optimization
Heavy data aggregation routines use sequential file streaming to keep operational memory costs flat during long-running tracking periods, essential for institutions with thousands of students.

### 🔐 Input Validation & Security
All text entries pass through strict string filter logic to block syntax anomalies and malicious character sequences before data reaches database nodes. RBAC ensures users only access authorized modules.

### 📊 Real-Time Analytics
Live dashboard updates reflect attendance, grades, and financial data in real-time with automated report generation.

### 📋 Module Execution Examples
## Attendance Processing


```bash

python3 attendance.py
# Output: attendance_log_2024.csv (morning and mid-day records)

```

## Grade Calculation

```bash

python3 metrices.py
# Output: weighted_grades.json (quiz + assignment + exam scores)

```


## Financial Reporting

```bash

python3 finance.py
# Output: billing_statements.pdf (tuition & concessions)

```

## Report Generation

```bash

python3 report.py
# Output: student_reports/ (individual progress cards)

```


### 🎯 Islamic Education Features
Hifz Tracking
Monitor Quran memorization progress
Track surah completion
Measure recitation accuracy
Automatic proficiency levels
Tarbiyah Modules
Character development tracking
Islamic values assessment
Behavioral monitoring
Progress visualization
### 📞 Support & Documentation
For implementation details, see:

Database schema: database.sql
API endpoints: Refer to Management.js
Configuration: Check config.py (Python modules)
### 📄 License
This project is developed for Al-Noor Islamic Academy. Contact institution for usage rights.

Built with ❤️ for Islamic Education Excellence
