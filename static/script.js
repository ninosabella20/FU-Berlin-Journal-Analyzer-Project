let journalEntries = JSON.parse(localStorage.getItem('journalEntries')) || [];

function saveJournalEntry(entry) {
  console.log("event: "+ entry)
  const date = new Date().toLocaleDateString();
  journalEntries.push({ date, content: entry });
  localStorage.setItem('journalEntries', JSON.stringify(journalEntries));
  updateJournalList();
  updateCharts();
  fetch('/submit', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({text: entry})
            })
            .then(response => response.json())
            .then(data => {
                alert('Journal saved: ' + data.status);
            });
}

function updateJournalList() {
  const journalList = document.getElementById('journalList');
  if (journalList) {
    journalList.innerHTML = '';
    journalEntries.forEach(entry => {
      const li = document.createElement('li');
      li.textContent = `${entry.date}: ${entry.content.substring(0, 20)}...`;
      journalList.appendChild(li);
    });
  }
  const historyList = document.getElementById('historyList');
  if (historyList) {
    historyList.innerHTML = '';
    journalEntries.forEach(entry => {
      const li = document.createElement('li');
      li.textContent = `${entry.date}: ${entry.content.substring(0, 20)}...`;
      historyList.appendChild(li);
    });
  }
}

function calculateWordCounts() {
  const wordCounts = [0, 0, 0, 0, 0, 0];
  journalEntries.forEach(entry => {
    const day = new Date(entry.date).getDay();
    const words = entry.content.split(/\s+/).length;
    wordCounts[day] += words;
  });
  return wordCounts;
}

function updateCharts() {
  const wordCounts = calculateWordCounts();
  const wordCountData = {
    labels: ['M', 'T', 'W', 'T', 'F', 'S'],
    datasets: [{
      label: 'Words',
      data: wordCounts,
      backgroundColor: 'rgba(75, 192, 192, 0.2)',
      borderColor: 'rgba(75, 192, 192, 1)',
      borderWidth: 1
    }]
  };

  const heatMapData = {
    labels: ['M', 'T', 'W', 'T', 'F', 'S'],
    datasets: [{
      label: 'Heat',
      data: wordCounts,
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
      borderColor: 'rgba(255, 99, 132, 1)',
      borderWidth: 1
    }]
  };

  const wordCountChart = document.getElementById('wordCountChart');
  if (wordCountChart) {
    new Chart(wordCountChart.getContext('2d'), {
      type: 'bar',
      data: wordCountData,
      options: { scales: { y: { beginAtZero: true } } }
    });
  }

  const heatMap = document.getElementById('heatMap');
  if (heatMap) {
    new Chart(heatMap.getContext('2d'), {
      type: 'bar',
      data: heatMapData,
      options: { scales: { y: { beginAtZero: true } } }
    });
  }
}


updateJournalList();
updateCharts();