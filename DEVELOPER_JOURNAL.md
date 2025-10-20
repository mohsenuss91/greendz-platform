# GreenDZ Developer Journal

This journal documents the development process of the GreenDZ platform, providing a clear and shareable log of tasks, decisions, and outcomes.

---

### **2025-10-20T11:00:00Z — Milestone 1: Project Scaffolding & Documentation**

*   **Task:** Initial Project Setup, First Commit, and Push to GitHub
*   **Status:** **COMPLETE**
*   **Commands Executed:**
    *   `git init`
    *   `git config user.name "mdouaour"`
    *   `git config user.email "yacine23i@hotmail.com"`
    *   Branch creation and merging
    *   `git remote add origin git@github.com:mdouaour/greendz-platform.git`
    *   `git push -u origin main`
    *   `git push -u origin dev`
    *   `git tag -a v0.1.0 -m "..."`
    *   `git push --tags`
*   **Git Commits:** `e0e0120`, `11c9b7a`
*   **Git Tag:** `v0.1.0`
*   **Rationale:** This step established the foundational structure of the project. It set up the Git repository, created the necessary branches, scaffolded the directory and documentation structure, and recorded everything in the first commit. Pushing to GitHub and tagging the release marks the successful completion of the first milestone.
*   **Next Steps:** Begin Milestone 2: Backend MVP development.

---

### **2025-10-20T12:00:00Z — Milestone 2: Backend MVP (Flask & SQLite)**

*   **Task:** Backend API Development
*   **Status:** **COMPLETE**
*   **Commands Executed:**
    *   `git checkout -b feature/backend-mvp`
    *   `pip install -r requirements.txt`
    *   `flask db init`, `flask db migrate`, `flask db upgrade`
    *   `pytest`
    *   `git add .`
    *   `git commit -m "feat(backend): implement backend mvp with tree api" ...`
    *   `git commit --amend --no-edit`
*   **Files Created/Modified:**
    *   `backend/app.py`
    *   `backend/requirements.txt`
    *   `backend/migrations/`
    *   `backend/tests/test_api.py`
    *   `backend/.gitignore`
*   **Git Commit:** `7125e82`
*   **Rationale:** This milestone delivered the core backend functionality. It includes a working Flask server, a SQLite database with User and Tree models, and a REST API for creating and retrieving trees. Unit tests were also added to ensure the API's reliability. This work is now ready to be consumed by the frontend.
*   **Next Steps:** Merge the `feature/backend-mvp` branch into `dev` and begin Milestone 3: Frontend MVP development.