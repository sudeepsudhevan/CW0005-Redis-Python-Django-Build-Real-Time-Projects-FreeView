document.addEventListener("DOMContentLoaded", function() {
    const wrapper = document.getElementById("live-poll-results");
    const resultsDiv = document.getElementById("poll-results-content")

    if (!wrapper || !resultsDiv) return;

    const pollId = wrapper.dataset.pollId;
    
    if (!pollId) {
        resultsDiv.innerHTML = "<p>Error: Poll ID not found.</p>";
        return;
    }

    async function fetchPollResults() {
        try {
            const response = await fetch(`/api/polls/${pollId}/results`);
            const data = await response.json();
            
            if (data.results && data.options) {
                let html = "<ul>";
                for (const option of data.options) {
                    const count = data.results[option.id] || 0;
                    html += `<li><strong>${option.text}:</strong> ${count} votes</li>`;
                }
                html += "</ul>";
                
                html += `<p><strong>Total Votes:</strong> ${data.total_votes}</p>`;
                if('unique_voters' in data) {
                    html += `<p><strong>Unique Voters:</strong> ${data.unique_voters}</p>`;
                }
                resultsDiv.innerHTML = html;
            } else {
                resultsDiv.innerHTML = "<p>No results available.</p>";
            }

        } catch (error) {
            console.error("Error fetching results:", error);
            resultsDiv.innerHTML = "<p>Error fetching poll results. Please try again later.</p>";
        }
    }

    // Initial fetch + every 5 seconds
    fetchPollResults();
    setInterval(fetchPollResults, 5000);
})
