package com.sidpatchy.romebot.Embed;

import org.javacord.api.entity.message.embed.EmbedBuilder;
import org.javacord.api.entity.server.Server;
import org.javacord.api.entity.user.User;

import java.awt.*;
import java.time.Instant;

public class JoinedEmbed {
    public static EmbedBuilder getJoined(User user, Server server) {
        //long time = Timestamp.from(user.getJoinedAtTimestamp(server));
        Instant instant = user.getJoinedAtTimestamp(server).orElse(null);
        if (instant == null) {instant = Instant.EPOCH;}
        long timestamp = instant.toEpochMilli();
        return new EmbedBuilder()
                .setColor(Color.decode("#e74d3c"))
                .setAuthor(user.getDisplayName(server), "", user.getAvatar())
                .setDescription(String.format("<t:%ts>", timestamp));
    }
}
