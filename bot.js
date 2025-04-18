const mineflayer = require('mineflayer');
const fs = require('fs');
const chalk = require('chalk');

const ip = process.argv[2];
const port = parseInt(process.argv[3]);

function createBot(id) {
    const bot = mineflayer.createBot({
        host: ip,
        port: port,
        username: `Bot${id}`
    });

    bot.on('login', () => {
        console.log(chalk.green(`[JS] Bot${id} logged in.`));
    });

    bot.on('chat', (username, message) => {
        if (message.includes('/login')) {
            bot.chat('/login 8000! 8000!');
        } else if (message.includes('/register')) {
            bot.chat('/register 8000! 8000!');
        }
    });

    bot.once('spawn', () => {
        watchMovement(bot);
    });
}

function watchMovement(bot) {
    setInterval(() => {
        fs.readFile('movement.txt', 'utf8', (err, data) => {
            if (err) return;
            const move = data.trim();

            if (move === "jump") {
                bot.setControlState('jump', true);
                setTimeout(() => bot.setControlState('jump', false), 500);
            } else {
                bot.setControlState(move, true);
                setTimeout(() => bot.setControlState(move, false), 500);
            }
        });
    }, 1500);
}

// 🧨 Launch multiple bots
for (let i = 0; i < 5; i++) {
    setTimeout(() => createBot(i), i * 1000);
}