package com.sidpatchy.romebot.Embed;

import org.javacord.api.entity.message.embed.EmbedBuilder;
import org.javacord.api.entity.server.Server;
import org.javacord.api.entity.user.User;

import java.awt.*;
import java.util.Locale;

public class AssassinateEmbed {
    public static EmbedBuilder getAssassinate(User user, Server server) {
        return new EmbedBuilder()
                .setColor(Color.decode("#e74d3c"))
                .setImage("https://i.imgur.com/BZa1oge.jpeg")
                .setAuthor("WHOOP! WHOOP! " + user.getDisplayName(server).toUpperCase() + " HAS BEEN ASSASSINATED!", "", user.getAvatar());
    }
}
