package com.sidpatchy.romebot.Embed;

import com.sidpatchy.romebot.Main;
import org.javacord.api.entity.message.embed.EmbedBuilder;
import org.javacord.api.entity.server.Server;
import org.javacord.api.entity.user.User;

public class JupiterHatesEmbed {

    public static EmbedBuilder getJupiterHates(User user, User author, Server server) {
        if (user == null) { user = author; }

        return new EmbedBuilder()
                .setColor(Main.getColour())
                .setImage("https://github.com/Sidpatchy/RomeBot/blob/151a9c28eb6cc735990686a62a90772fca93b238/bot/images/jupiter.jpg?raw=true")
                .setAuthor(user.getDisplayName(server).toUpperCase() + " offended the almighty Jupiter, they're now dead, press 'F' to pay respects", "", user.getAvatar());
    }
}
