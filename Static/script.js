document.getElementById('generateBtn').addEventListener('click', () => {
    const good = document.getElementById('goodMoral').value;
    const bad = document.getElementById('badMoral').value;

    if (!good && !bad) {
        alert("Please enter at least one moral.");
        return;
    }

    fetch("/generate-story/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie('csrftoken')
        },
        body: JSON.stringify({ good_moral: good, bad_moral: bad })
    })
    .then(response => response.json())
   .then(data => {
    const storyBox = document.getElementById("generatedStory");
    storyBox.innerText = data.story;
    storyBox.classList.remove("hidden");

    // Optional: clear input fields
    document.getElementById("goodMoral").value = "";
    document.getElementById("badMoral").value = "";
})

});

// Helper function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Fetch and load stories into dropdown on page load
window.addEventListener("DOMContentLoaded", () => {
    fetch("/get-stories/")
        .then(response => response.json())
        .then(data => {
            const select = document.getElementById("storySelect");
            select.innerHTML = '<option>Select a story</option>';
            data.stories.forEach(story => {
                const option = document.createElement("option");
                option.value = story.text;
                option.textContent = story.label || "Untitled Story";
                select.appendChild(option);
            });
        });
});

// Show story when selected
document.getElementById("storySelect").addEventListener("change", (e) => {
    const selectedStory = e.target.value;
    if (selectedStory && selectedStory !== "Select a story") {
        const storyBox = document.getElementById("generatedStory");
        storyBox.innerText = selectedStory;
        storyBox.classList.remove("hidden");
    }
});
