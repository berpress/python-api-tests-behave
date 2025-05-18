# API Testing Project with Behave and Requests

This project demonstrates API testing using Python's [Behave](https://behave.readthedocs.io/) BDD framework together with the `requests` library.

---

## 🚀 Features

- **API Client** using `requests.Session` for efficient HTTP calls
- Reusable **BDD Steps** with clear separation of concerns
- Response validation with Python **dataclasses**
- Flexible environment configuration (dev, stage, prod)
- Detailed **request/response logging** for better debugging

---

⚙️ Setup

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

🧪 Running Tests

```bash
behave
```

🐳 Use Docker to run the local API client:

```bash
docker run -d -p 56733:80 litovsky/flask-api-test
```

This command will start the API service in a Docker container, exposing port 56733 on your machine.

You can verify it by opening: http://localhost:56733 in your browser or via API requests.


