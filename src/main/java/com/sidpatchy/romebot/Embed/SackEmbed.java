package com.sidpatchy.romebot.Embed;

import com.sidpatchy.romebot.Main;
import org.javacord.api.entity.message.embed.EmbedBuilder;
import org.javacord.api.entity.server.Server;
import org.javacord.api.entity.user.User;

public class SackEmbed {
    public static EmbedBuilder getSacked(User user, User author, Server server) {
        if (user == null) { user = author; }

        return new EmbedBuilder()
                .setColor(Main.getColour())
                .setImage("https://github.com/Sidpatchy/RomeBot/blob/151a9c28eb6cc735990686a62a90772fca93b238/bot/images/sacked.jpg?raw=true")
                .setAuthor("OOOOHHHH FUK! " + user.getDisplayName(server).toUpperCase() + " GOT THE SACK!", "", user.getAvatar())
                .setDescription("Okay okay okay, this really needs to be explained to make any sense. This command is " +
                        "in reference to poena cullei which constituted being blindfolded, being told you were unworthy " +
                        "of light, being taken to a field and beat until one couldn\\'t take it anymore, then, I SHIT " +
                        "YOU NOT, being thrown into a sack along with a serpent, an ape, a dog, and a rooster, then it " +
                        "was sewed up, THEN MOTHERFUCKER, being thrown into the sea.");
    }
}
