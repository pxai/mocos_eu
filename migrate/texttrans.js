const translate = require('./translate.js');
const fs = require('fs');

if (!process.argv[2] || !process.argv[3]) {
  console.error('Please provide a folder to translate and destiny');
  process.exit(1);
}

translateFile().then(result => {
  console.log('About to start');
})



async function translateFile() {
  file = 'html-to-markdown(4).md';
  const processFolder = process.argv[2];
  const destinyFolder = process.argv[3];

  //fs.readdirSync(processFolder).forEach(async file => {
    console.log(file);
    const code = fs.readFileSync(`${processFolder}/${file}`, { encoding: 'utf8', flag: 'r' });

    const lines = code.split('\n');

    console.log('AbOut to read lines: ', lines.length);

    let insideCodeBlock = false;
    const codeBlockRegex = /^```/;
    const resultLine = [];
    let textBlock = "";

    for (let line of lines) {
      line = line.trim(); // Remove leading and trailing whitespace

      if (codeBlockRegex.test(line.trim())) {
        if (line.trim().startsWith('```Python') || line.trim().startsWith('```console')) {
          const translatedLine = await translate(textBlock);
          resultLine.push(translatedLine);
          //resultLine.push("TR" + textBlock + "END_TR");
          textBlock = "";
        }
        resultLine.push(line);
        insideCodeBlock = !insideCodeBlock;
      } else {
        if (!insideCodeBlock) {
          textBlock += line + "\n";
        } else {
          resultLine.push(line);
        }
      }

      console.log('Line processed: ', line);

     /*  if (shouldIgoreLine(insideCodeBlock, line)) {
        resultLine.push(line);
      } else {
        translatedLine = "TR> " +  line;
        //const translatedLine = await translate(line)
        resultLine.push(translatedLine)
      } */
    }

    //
    console.log("TRANSLATED CODE: \nSize: ", resultLine.length, " lines \n");
    fs.writeFileSync(`${destinyFolder}/${file}`, resultLine.join('\n'));
    // await sleep(2000);
  //});
}

function shouldIgoreLine(insideCodeBlock, line) {
  if (line.trim().startsWith('```')) return true;
  if (insideCodeBlock) return true;
  if (line.trim() === '') return true;
  if (line.trim().startsWith('![](')) return true;
  if (line.trim().startsWith('----')) return true;

  return false;
}


function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}