async function askAI() {
    const question = document.getElementById("question").value;
    const answerElement = document.getElementById("answer");

    if (!question.trim()) {
        answerElement.innerText = "Please enter a question.";
        return;
    }

    answerElement.innerText = "Thinking...";

    try {
        const response = await fetch("http://127.0.0.1:8000/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: question
            })
        });

        const data = await response.json();
        answerElement.innerText = data.answer;

        // AI answer ko awaaz mein bolo
        const speech = new SpeechSynthesisUtterance(data.answer);
        speech.lang = "en-US";
        window.speechSynthesis.speak(speech);

    } catch (error) {
        answerElement.innerText = "Could not connect to the AI server.";
        console.error(error);
    }
}


function startListening() {
    const statusElement = document.getElementById("status");
    const questionInput = document.getElementById("question");

    const SpeechRecognition =
        window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
        statusElement.innerText =
            "Voice recognition is not supported in this browser.";
        return;
    }

    const recognition = new SpeechRecognition();

    recognition.lang = "en-US";
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    statusElement.innerText = "Listening... Speak now 🎤";

    recognition.start();

    recognition.onresult = function (event) {
        const spokenText = event.results[0][0].transcript;

        questionInput.value = spokenText;
        statusElement.innerText = "You said: " + spokenText;

        // Automatically AI ko question bhejo
        askAI();
    };

    recognition.onerror = function (event) {
        statusElement.innerText =
            "Voice error: " + event.error;
    };

    recognition.onend = function () {
        if (statusElement.innerText === "Listening... Speak now 🎤") {
            statusElement.innerText = "";
        }
    };
}