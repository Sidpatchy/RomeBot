package com.sidpatchy.romebot.Embed;

import com.sidpatchy.romebot.Main;
import org.apache.commons.lang3.time.DurationFormatUtils;
import org.javacord.api.entity.message.embed.EmbedBuilder;
import org.javacord.api.entity.server.Server;
import org.javacord.api.entity.user.User;

import java.time.Instant;

public class JoinedEmbed {
    public static EmbedBuilder getJoined(User user, User author, Server server) {
        if (user == null) { user = author; }

        Instant instant = user.getJoinedAtTimestamp(server).orElse(null);
        if (instant == null) {instant = Instant.EPOCH;}
        long timestamp = instant.toEpochMilli();

        String timeSinceJoin;
        if (server == null) {
            timeSinceJoin = DurationFormatUtils.formatDurationWords(System.currentTimeMillis() - user.getCreationTimestamp().toEpochMilli(), true, false);
        }
        else {
            timeSinceJoin = DurationFormatUtils.formatDurationWords(System.currentTimeMillis() - user.getJoinedAtTimestamp(server).orElse(Instant.ofEpochMilli(0)).toEpochMilli(), true, false);
        }

        return new EmbedBuilder()
                .setColor(Main.getColour())
                .setAuthor(user.getDisplayName(server), "", user.getAvatar())
                .setDescription("Joined on " + String.format("<t:%ts>", timestamp) + "\n*" + timeSinceJoin + "*");
    }
}
