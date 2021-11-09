package com.sidpatchy.romebot.Embed;

import org.javacord.api.entity.message.embed.EmbedBuilder;

import java.awt.*;

public class CarthagoDelandaEstEmbed {
    public static EmbedBuilder getCarthago() {
        return new EmbedBuilder()
                .setColor(Color.decode("#e74d3c"))
                .setAuthor("Ceterum autem censeo Carthaginem esse delendam")
                .setImage("https://i.imgur.com/PuFJRwT.jpeg");
    }
}
