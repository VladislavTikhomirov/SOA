// Toggle dark mode
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
}

// Send message to Flask backend
function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    const chatBox = document.getElementById("chat-box");

    // Append user input to chat
    chatBox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;

    // Send user input to Flask backend
    fetch('/send_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Append AI response to chat
        chatBox.innerHTML += `<p><strong>AI:</strong> ${data.response}</p>`;
        document.getElementById("user-input").value = ""; // Clear input
        chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to bottom
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Toggle dynamic menu visibility
function toggleMenu() {
    const menu = document.getElementById('menu-container');
    if (menu.style.display === 'none' || menu.style.display === '') {
        menu.style.display = 'block';
    } else {
        menu.style.display = 'none';
    }
}

// Function to simulate switching AI models
function changeModel(model) {
    fetch('/change_model', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ model: model })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.status); // Notify user about model change
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
