package com.sidpatchy.romebot.Embed;

import org.javacord.api.entity.message.embed.EmbedBuilder;
import org.javacord.api.entity.server.Server;
import org.javacord.api.entity.user.User;

import java.awt.*;

public class ImpaleEmbed {
    public static EmbedBuilder getImpaled(User user, User author, Server server) {
        if (user == null) { user = author; }

        return new EmbedBuilder()
                .setColor(Color.decode("#e74d3c"))
                .setAuthor(user.getDisplayName(server).toUpperCase() + " has been impaled!", "", user.getAvatar())
                .setImage("https://i.imgur.com/5SFE9pt.jpeg");
    }
}
