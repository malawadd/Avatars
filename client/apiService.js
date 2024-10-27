const axios = require('axios');

const baseURL = 'http://localhost:5450';

const api = axios.create({
  baseURL,
  //   timeout: 5000, // Set a timeout for requests (optional)
});

const screenshot= async() => {
  try {
    const response = await api.get(`/screenshot`);
    return response
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error
  }
}



const conversation = (prompt) => {
  return new Promise((resolve, reject) => {
    let endpoint = '/chat';
    
    console.log(`Sending to endpoint ${endpoint}: ${prompt}`);
    api.get(endpoint, { params: { prompt } })
      .then(response => {
        console.log(response.data.response)
        resolve(response);
      })
      .catch(error => {
        console.error('Error fetching conversation:', error);
        reject(error);
      });
  });
};

module.exports = {
  screenshot,
  conversation
}
