package com.sidpatchy.romebot.Embed;

import com.sidpatchy.romebot.Main;
import org.javacord.api.DiscordApi;
import org.javacord.api.entity.message.embed.EmbedBuilder;

import java.awt.*;

public class InfoEmbed {
    public static EmbedBuilder getInfo(DiscordApi api) {
        return new EmbedBuilder()
                .setColor(Main.getColour())
                .addField("Need Help?", "You can get help by creating an issue on our [GitHub](https://github.com/Sidpatchy/RomeBot/issues) or by joining our [support server](https://discord.gg/NwQUkZQ)", true)
                .addField("Add Me to a Server", "Adding me to a server is simple, all you have to do is click [here](https://discord.com/oauth2/authorize?client_id=511050489928876052&scope=bot&permissions=0)", true)
                .addField("GitHub", "RomeBot is open source, that means you can view all of its code! Check out its [GitHub!](https://github.com/Sidpatchy/RomeBot)", true)
                .addField("Server Count", "I have enlightened **" + api.getServers().size() + "** servers.", true)
                .addField("Version", "I am running RomeBot **v3.0-a.4**, released on **2022-09-26**", true);
    }
}
