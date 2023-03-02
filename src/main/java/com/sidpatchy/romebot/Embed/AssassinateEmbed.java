package com.sidpatchy.romebot.Embed;

import com.sidpatchy.romebot.Main;
import org.javacord.api.entity.message.embed.EmbedBuilder;
import org.javacord.api.entity.server.Server;
import org.javacord.api.entity.user.User;

public class AssassinateEmbed {
    public static EmbedBuilder getAssassinate(User user, User author, Server server) {
        if (user == null) { user = author; }

        return new EmbedBuilder()
                .setColor(Main.getColour())
                .setImage("https://i.imgur.com/BZa1oge.jpeg")
                .setAuthor("WHOOP! WHOOP! " + user.getDisplayName(server).toUpperCase() + " HAS BEEN ASSASSINATED!", "", user.getAvatar());
    }
}
