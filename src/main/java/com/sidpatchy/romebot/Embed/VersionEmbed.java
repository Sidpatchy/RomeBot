package com.sidpatchy.romebot.Embed;

import org.javacord.api.entity.message.embed.EmbedBuilder;

import java.awt.*;

public class VersionEmbed {
    public static EmbedBuilder getVersion() {
        return new EmbedBuilder()
                .setColor(Color.decode("#e74d3c"))
                .addField("RomeBot v3.0", "Released: 2021-10-01");
    }
}
