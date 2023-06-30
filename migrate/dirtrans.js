const translate = require('./translate.js');
const fs = require('fs');

if (!process.argv[2] || !process.argv[3]) {
  console.error('Please provide a folder to translate and destiny');
  process.exit(1);
}

const processFolder = process.argv[2];
const destinyFolder = process.argv[3];

fs.readdirSync(processFolder).forEach(async file => {
  console.log(file);
  const code = fs.readFileSync(`${processFolder}/${file}`, { encoding: 'utf8', flag: 'r' });
  const translatedCode = await translate(code)
  console.log("TRANSLATED CODE: \n", translatedCode);
  fs.writeFileSync(`${destinyFolder}/${file}`, translatedCode);
  await sleep(2000);
});


function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}