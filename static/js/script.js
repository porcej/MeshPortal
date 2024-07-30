document.addEventListener('DOMContentLoaded', (event) => {
    fetchMessages();
    setInterval(fetchMessages, 5000);
});

function fetchMessages() {
    fetch('/messages')
        .then(response => response.json())
        .then(data => {
            const messageList = document.getElementById('messageList');
            messageList.innerHTML = '';
            data.forEach(message => {
                const li = document.createElement('li');
                li.textContent = message;
                messageList.appendChild(li);
            });
        });
}

function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const message = messageInput.value;

    fetch('/send', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        messageInput.value = '';
        fetchMessages();
    });
}
