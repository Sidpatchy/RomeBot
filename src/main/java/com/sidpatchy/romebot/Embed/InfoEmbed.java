package com.sidpatchy.romebot.Embed;

import org.javacord.api.entity.message.embed.EmbedBuilder;

import java.awt.*;

public class InfoEmbed {
    public static EmbedBuilder getInfo() {
        return new EmbedBuilder()
                .setColor(Color.decode("#e74d3c"))
                .addField("Need Help?", "You can get help by creating an issue on our [GitHub](https://github.com/Sidpatchy/RomeBot/issues) or by joining our [support server](https://discord.gg/NwQUkZQ)", true)
                .addField("Add Me to a Server", "Adding me to a server is simple, all you have to do is click [here](https://discord.bots.gg/bots/511050489928876052)", true)
                .addField("GitHub", "RomeBot is open source, that means you can view all of its code! Check out its [GitHub!](https://github.com/Sidpatchy/RomeBot)", true);
    }
}
