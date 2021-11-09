package com.sidpatchy.romebot.Embed;

import org.javacord.api.DiscordApi;
import org.javacord.api.entity.message.embed.EmbedBuilder;

import java.awt.*;

public class ServersEmbed {

    public static EmbedBuilder getServers(DiscordApi api) {
        return new EmbedBuilder()
                .setColor(Color.decode("#e74d3c"))
                .addField("Servers Enlightened", String.valueOf(api.getServers().size()));
    }
}
