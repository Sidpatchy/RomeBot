package com.sidpatchy.romebot.Embed;

import com.sidpatchy.romebot.Main;
import org.javacord.api.entity.message.embed.EmbedBuilder;
import org.javacord.api.entity.server.Server;
import org.javacord.api.entity.user.User;

import java.awt.*;
import java.time.Instant;

public class JoinedEmbed {
    public static EmbedBuilder getJoined(User user, User author, Server server) {
        if (user == null) { user = author; }

        Instant instant = user.getJoinedAtTimestamp(server).orElse(null);
        if (instant == null) {instant = Instant.EPOCH;}
        long timestamp = instant.toEpochMilli();

        return new EmbedBuilder()
                .setColor(Main.getColour())
                .setAuthor(user.getDisplayName(server), "", user.getAvatar())
                .setDescription("Joined on " + String.format("<t:%ts>", timestamp));
    }
}
