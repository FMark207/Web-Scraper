fetch('data.json')
  .then(response => response.json()) // Parse the JSON response
  .then(data => {
    // Your data is now in the 'data' variable (usually an object or array)
    console.log(data);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });