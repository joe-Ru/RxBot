import DISCORD_TOKEN from "./token.js";
import Discord from "discord.js";
import fetch from "node-fetch";
import axios from "axios";

const client = new Discord.Client();

const prefix = '!';
const MED_ANNOUNCEMENT = "The RxBot is not to be taken as medical advice, if you are in trouble\
please contact your physician or call 911 if this is a medical emergency. ";

client.on('ready', () => {
    console.log("Connected as " + client.user.tag)
})

//Urban dictionary command
client.on('message', async message => {
	if (!message.content.startsWith(prefix) || message.author.bot) return;

	const args = message.content.slice(prefix.length).split(/ +/);
	const command = args.shift().toLowerCase();
  const querystring = require('querystring');

  // Start of Urban command
  if (command === 'urban') {
    if (!args.length) {
      return message.channel.send('You need to supply a search term!');
    }

	const query = querystring.stringify({ term: args.join(' ') });

  const { list } = await fetch(`https://api.urbandictionary.com/v0/define?${query}`).then(response => response.json());
  
  if (!list.length) {
    return message.channel.send(`No results found for **${args.join(' ')}**.`);
  }
  
  message.channel.send(list[0].definition);
  } // end of Urban command	
});


// #### CAT FACT/PICTURE FUNCTIONALITY ####
//Sends picture of a cat
const sendCats = async (message, numCats) => {
  const catImages = (await axios.get(`https://api.thecatapi.com/v1/images/search?limit=${numCats}`)).data;
  for (const catImage of catImages) {
    message.channel.send(new Discord.Attachment(catImage.url));
  }
}

// Calls on the sendCats 'function
client.on('message', message => {
    if (message.content === '!cat') {
      sendCats(message, 1);
    } else if (/^!cat [0-9]*$/.test(message.content)) {
      let numberOfCats = message.content.split(' ')[1];
      if (numberOfCats > 10 || numberOfCats < 1) {
        numberOfCats = 1;
      }
      sendCats(message, numberOfCats);
    }
  });

//Prints out cat fact
client.on('message', async message => {
  if(message.content == '!catFact') {
    const { fact } = await fetch('https://catfact.ninja/fact').then(response => response.json());
    message.channel.send(fact);
  }
})



client.on('message', async message => {
  
  if(message.content === '!medFact'){

    //TODO: Look into parsing the JSON output from the API to a variable and then accessing the info from there.
    const args = message.content.slice(prefix.length).split(/ +/);
    const command = args.shift().toLowerCase();
    const querystring = require('querystring');
  
    // Start of Urban command
    if (command === 'medFact') {
      if (!args.length) {
        return message.channel.send('You need to supply a search term!');
      }
  
    const query = querystring.stringify({ term: args.join(' ') });
  
    const { list } = await fetch(`https://api.fda.gov/drug/event.json?search=${query}`).then(response => response.json());
    
    if (!list.length) {
      return message.channel.send(`No results found for **${args.join(' ')}**.`);
    }
    
    message.channel.send(MED_ANNOUNCEMENT);
    message.channel.send(list[0].definition);
  }
}
})

  /* Look into this.
client.on('message', (receivedMessage) => {
    if (receivedMessage.author == client.user) {
        return
    }

    receivedMessage.channel.send("Message received: " + receivedMessagae.author.toString() + receivedMessage.content)
})
Use this for drug API https://api.fda.gov/drug/event.json?limit=1
*/ 

client.login(DISCORD_TOKEN);
