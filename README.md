# 🎙️ Voice Assistant App (React + Flask + Vapi + GPT-5)

A full-stack **voice assistant application** built with **Vite + React** on the frontend and **Flask** on the backend, integrated with **Vapi** and powered by **GPT-5**.
The app allows users to fill in personal details and then engage in a **voice-based conversation** with a GPT-5-powered assistant configured with specific objectives, for example, evaluating if the user is a good fit for a certain **job** or **program**.
After the call ends, the app automatically generates and displays a **summary of the conversation**.

---

## ✨ Features

* **User Information Form**
  Collects first name, last name, email, and phone number before the conversation begins.

* **Voice-Based Interaction**
  The assistant talks with the user in real time, powered by **Vapi Agent** and **ChatGPT-5**.

* **Custom Assistant Behavior**
  Configurable prompts and objectives — for example, screening for a specific role or program.

* **Automated Conversation Summary**
  After the call ends, a concise summary is displayed in the app.

* **Full-Stack Architecture**

  * **Frontend**: Vite + React for fast and responsive UI.
  * **Backend**: Flask API to handle Vapi integration and server-side logic.

---

## 🛠️ Tech Stack

**Frontend**

* [Vite](https://vitejs.dev/)
* [React](https://react.dev/)
* [Axios](https://axios-http.com/) (for API requests)
* \[CSS / TailwindCSS] (optional styling choice)

**Backend**

* [Flask](https://flask.palletsprojects.com/)
* [Vapi](https://vapi.ai/) (Voice AI API)
* [OpenAI GPT-5](https://platform.openai.com/) integration

---

## 📂 Project Structure

```
voice-assistant-app/
│
├── frontend/            # Vite + React app
│   ├── src/
│   ├── package.json
│   └── vite.config.js
│
├── backend/             # Flask API
│   ├── app.py
│   ├── requirements.txt
│   └── vapi_integration.py
│
├── README.md
└── .gitignore
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2️⃣ Setup Backend (Flask)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Run the backend:

```bash
python app.py
```

### 3️⃣ Setup Frontend (Vite + React)

```bash
cd frontend
npm install
npm run dev
```

---

## ⚙️ Environment Variables

Create a `.env` file in your **backend** folder with:

```
VAPI_API_KEY=your_vapi_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 🎯 Example Use Case

1. User visits the web app and fills out the form with personal details.
2. The assistant starts a **real-time voice conversation**.
3. The assistant’s behavior is based on **custom prompts** (e.g., job/program eligibility screening).
4. Once the call ends, the system generates a **summary** of the conversation.

---

## 📸 Screenshots

*(Add screenshots or GIFs here to showcase the app)*

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 👨‍💻 Author

**Taha Naguez** – [GitHub](https://github.com/tahangz)
