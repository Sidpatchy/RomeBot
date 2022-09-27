package com.sidpatchy.romebot.Embed;

import com.sidpatchy.romebot.Main;
import org.javacord.api.entity.message.embed.EmbedBuilder;

import java.awt.*;
import java.time.Instant;

public class TimeEmbed {
    public static EmbedBuilder getTime() {
        return new EmbedBuilder()
                .setColor(Main.getColour())
                .addField("Time", "<t:" + Instant.now().getEpochSecond() + ">");
    }
}
