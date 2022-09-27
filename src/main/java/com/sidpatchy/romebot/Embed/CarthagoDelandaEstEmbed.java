package com.sidpatchy.romebot.Embed;

import com.sidpatchy.romebot.Main;
import org.javacord.api.entity.message.embed.EmbedBuilder;

import java.awt.*;

public class CarthagoDelandaEstEmbed {
    public static EmbedBuilder getCarthago() {
        return new EmbedBuilder()
                .setColor(Main.getColour())
                .setAuthor("Ceterum autem censeo Carthaginem esse delendam")
                .setImage("https://i.imgur.com/PuFJRwT.jpeg");
    }
}
