const a=1

while (a=1)
const apiKey = 'XWXORHP1704KVJ0K';
      const channelId = '2141717';
      const fieldId = '1';

      const url = `https://api.thingspeak.com/channels/${channelId}/fields/${fieldId}/last.json?api_key=${apiKey}`;

      fetch(url)
        .then(response => response.json())
        .then(data => {
          let value = data[fieldId];
          let valueElement = document.getElementById('demo');
          valueElement.textContent = value;
          alert(value)
        })
        .catch(error => console.error(error));
    

    