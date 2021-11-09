package com.sidpatchy.romebot.Embed;

import org.javacord.api.entity.message.embed.EmbedBuilder;

import java.awt.*;
import java.time.Instant;

public class TimeEmbed {
    public static EmbedBuilder getTime() {
        return new EmbedBuilder()
                .setColor(Color.decode("#e74d3c"))
                .addField("Time", "<t:" + Instant.now().getEpochSecond() + ">");
    }
}
