package com.sidpatchy.romebot.Embed;

import com.sidpatchy.romebot.Main;
import org.javacord.api.entity.message.embed.EmbedBuilder;
import org.javacord.api.entity.server.Server;
import org.javacord.api.entity.user.User;

public class StabEmbed {
    public static EmbedBuilder getStabbed(User user, User author, Server server) {
        if (user == null) { user = author; }

        return new EmbedBuilder()
                .setColor(Main.getColour())
                .setImage("https://github.com/Sidpatchy/RomeBot/blob/151a9c28eb6cc735990686a62a90772fca93b238/bot/images/stab.jpg?raw=true")
                .setAuthor(user.getDisplayName(server).toUpperCase() + " HAS BEEN STABBED!!!!", "", user.getAvatar())
                .setDescription("QUICK ALERT THE SENATE! oh wait... THE BASTARDS!");
    }
}
