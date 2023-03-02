package com.sidpatchy.romebot.Embed;

import com.sidpatchy.romebot.Main;
import org.javacord.api.entity.message.embed.EmbedBuilder;
import org.javacord.api.entity.server.Server;
import org.javacord.api.entity.user.User;


public class CrucifyEmbed {
    public static EmbedBuilder getCrucify(User user, User author, Server server) {
        if (user == null) { user = author; }

        return new EmbedBuilder()
                .setColor(Main.getColour())
                .setAuthor(user.getDisplayName(server).toUpperCase() + " HAS BEEN CRUCIFIED!", "", user.getAvatar())
                .setImage("https://i.imgur.com/HPypWCl.jpeg");
    }
}
