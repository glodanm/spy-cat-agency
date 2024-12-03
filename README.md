# **Spy Cat Agency (SCA) Management System**

The **Spy Cat Agency (SCA)** Management System simplifies the agency's spying operations by providing a platform to manage cats, their missions, and their assigned targets. The system includes APIs to handle CRUD operations for spy cats, missions, and targets, as well as custom logic for notes and mission completion.
- [Test task description](https://develops.notion.site/Python-engineer-test-assessment-the-Spy-Cat-Agency-1220fe54b07b80e78dd3c411e1309210)

---

## **Features**

### **Spy Cats**
- Add, update, delete, and view spy cats.
- Attributes: `name`, `years_of_experience`, `breed`, `salary`.

### **Missions**
- Create missions with associated targets in a single request.
- Assign a cat to a mission (only one mission per cat at a time).
- Mark missions as completed when all targets are finished.
- List, update, and delete missions (missions cannot be deleted if assigned).

### **Targets**
- Each mission includes 1-3 targets.
- Attributes: `name`, `country`, `notes`, `completed`.
- Update notes on a target (notes are frozen if a target or mission is completed).
- Mark individual targets as completed.

---

## **Installation**

### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spy-cat-agency.git
   cd spy-cat-agency
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

---

## **API Endpoints**

### **Spy Cats**
- `GET /api/cats/` - List all cats.
- `POST /api/cats/` - Add a new cat.
- `GET /api/cats/:id/` - Retrieve a specific cat.
- `PUT /api/cats/:id/` - Update a specific cat.
- `DELETE /api/cats/:id/` - Delete a specific cat.

### **Missions**
- `GET /api/missions/` - List all missions.
- `POST /api/missions/` - Create a new mission with targets.
- `GET /api/missions/:id/` - Retrieve a specific mission.
- `PUT /api/missions/:id/` - Update a specific mission and its targets.
- `DELETE /api/missions/:id/` - Delete a mission (if unassigned).

### **Targets**
- `GET /api/targets/` - List all targets.
- `GET /api/targets/:id/` - Retrieve a specific target.

---

## **Postman Collection**

If you have a link to your Postman workspace instead of a file, you can include it in the README file like this:

---

## **Postman Collection**

To interact with the API, use the following Postman workspace:

- [Spy Cat Agency API - Postman Workspace](https://www.postman.com/restless-sunset-722669/maksym-glodan-spy-cat-agency-api/overview)

### How to Use:
1. Click the link above to access the Postman workspace.
2. Sign in to your Postman account (if required).
3. Explore the collection and start testing the API.

---
