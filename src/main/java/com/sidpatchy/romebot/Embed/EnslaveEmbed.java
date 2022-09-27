package com.sidpatchy.romebot.Embed;

import com.sidpatchy.romebot.Main;
import org.javacord.api.entity.message.embed.EmbedBuilder;
import org.javacord.api.entity.server.Server;
import org.javacord.api.entity.user.User;

public class EnslaveEmbed {
    public static EmbedBuilder getEnslave(User user, User author, Server server) {
        if (user == null) { user = author; }

        return new EmbedBuilder()
                .setColor(Main.getColour())
                .setImage("https://raw.githubusercontent.com/Sidpatchy/RomeBot/151a9c28eb6cc735990686a62a90772fca93b238/bot/images/enslave.jpg")
                .setAuthor("Stonks! " + user.getDisplayName(server).toUpperCase() + " HAS BEEN ENSLAVED!", "", user.getAvatar());
    }
}
