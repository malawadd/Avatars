

# Avatar: A Personal Desktop Assistant

**Avatar** is an intelligent, personal desktop assistant that roams the user’s screen, providing seamless interactions. It activates when the user presses `Ctrl + L`, allowing users to ask anything and receive responses instantly. Built using Electron for the client and swarmzero for the backend, Avatar offers a comprehensive, expandable platform with plans for future enhancements.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
  - [Client Setup](#client-setup)
  - [Backend Setup](#backend-setup)
- [Usage](#usage)
- [Roadmap](#roadmap)

## Features

- **Text-Based Interaction**:  Press `Ctrl + L` to summon Avatar and ask questions. Receive text-based responses for any queries.
- **Personalization**: Avatar roams the user’s desktop, adding an interactive and engaging element.
- **Multi-Agent Support**: Avatar can be expanded to include additional avatars, each capable of different tasks.

## Project Structure

- **Client**: Electron-based desktop client that manages user interactions and displays the avatar.
- **Backend**: FastAPI-based server that handles queries and responses, using the `swarmzero` and `langtrace-python-sdk` libraries for intelligent conversations.

## Installation and Setup

### 1. Prerequisites

- **Node.js** (v18 or higher)
- **Python** (3.9+)
- **Pip** (Python package manager)

### 2. Client Setup

1. **Navigate to the client directory**:
   ```bash
   cd client
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Run the client**:
   ```bash
   npm start
   ```

The Electron app will launch, showcasing the Avatar .

### 3. Backend Setup

1. **Navigate to the backend directory** 
   ```bash
   cd backend
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install backend dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend server**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 5450
   ```

The backend will now be running on `http://localhost:5450`.

## Usage

1. **Start the backend server**: Ensure the backend is running as described above.
2. **Launch the Electron client**: Open the Electron app as described in the Client Setup.
3. **Interact with Avatar**:
   - Press `Ctrl + L` to activate the input interface.
   - Ask any question, and Avatar will respond through a text-based answer in the interface.

## Roadmap

Future enhancements for Avatar include:

1. **Audio Support for Input**: Enable voice-based commands.
2. **Vision Capabilities**: Add the ability to analyze visual input.
3. **More Avatars**: Introduce additional avatars with different personalities and functions.
4. **User Dashboard**: Add a dashboard for managing user settings and preferences.
5. **Executable Format**: Package the project into an installable executable.
6. **Avatar Agents for Specific Tasks**: Allow avatars to perform specific tasks like checking emails, setting reminders, etc.
7. **Video Generation**: Enable video-based responses or interactions.
8. **Image Generation**: Allow the generation of images based on user queries.

