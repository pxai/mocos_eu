const axios = require('axios');
require('dotenv').config();

async function getChatResponse(message) {
  try {
    const response = await axios.post('https://api.openai.com/v1/chat/completions', {
      model: 'gpt-3.5-turbo',
      messages: [{ role: 'system', content: 'You are a helpful assistant.' }, { role: 'user', content: message }]
    }, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.OPEN_AI_API_KEY}` // Replace with your OpenAI API key
      }
    });

    return response.data.choices[0].message.content;
  } catch (error) {
    console.error('Error:', error.response.data);
    throw error;
  }
}

// Example usage
const translate = async (code) => {
  try {
    // const userInput = 'Please translate this python code into basque, dont uppercase variables:\n' + code;
    const userInput = 'Please translate text about programming into informal basque:\n' + code;
    const response = await getChatResponse(userInput);

    return response;
  } catch (error) {
    console.error('Error:', error);
    return error;
  }
};

module.exports = translate;