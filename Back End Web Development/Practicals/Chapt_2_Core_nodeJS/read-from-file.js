const fs = require('fs');

fs.writeFile('ok.txt', 'what the FUCK am i doing', (err) => {
    if (err) 
        console.log(err);       
        
    else {
        fs.readFile('./ok.txt', 'utf-8', (err, data) => {
            if (err) 
                console.log(err);
            else
                console.log(data);
        })
    }
})


 fs.readFile('./ok.txt','utf-8', function(err, data){
     if (err !== null) {
        //handle error
         console.log(err)
     }else
     console.log(data);
 })


console.log(fs.readFileSync('./test.txt', 'utf-8'));

//prefer reaedfile, async > sync
fs.readFile('./test.txt', (err, data) => {
    //check if err is defined
    if (err) {
        console.log(err);
        return;
    }
    //since there is no error, the data object should contain a value.
    console.log(data.toString());
});