const Discord = require('discord.js')
const client = new Discord.Client()
const axios = require('axios')

//Sends picture of a cat
const sendCats = async (message, numCats) => {
    const catImages = (await axios.get(`https://api.thecatapi.com/v1/images/search?limit=${numCats}`)).data;
    for (const catImage of catImages) {
      message.channel.send(new Discord.Attachment(catImage.url));
    }
  }

//TODO: Send cat fact as a test
const catFact = async(message) = > {
  const catFact = (await axios.get())
}

client.on('ready', () => {
    console.log("Connected as " + client.user.tag)

   // Use this to send picture on bootup: const attachment = new Discord.Attachment("")
})


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

  /*
client.on('message', (receivedMessage) => {
    if (receivedMessage.author == client.user) {
        return
    }

    receivedMessage.channel.send("Message received: " + receivedMessagae.author.toString() + receivedMessage.content)
})
*/
client.login("NjU1MjExMjY0MjAwNDA5MDkw.XgPilg.3pSFaWH0P6brFDzKRxjdTIDAzaQ")