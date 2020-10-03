# Assembly Line tool development: Cosigners

Allow user to send out links for cosigners to sign on their own devices.

The first iteration has used two separate interviews - one for the user and another for all cosigners.

The interview also allows for a limited device choice. Everyone who signs is, if starting on a pc, given a choice to send a link to a mobile device

## TODO (Possibly)
1. Experiment with new `session_local` feature and its friends to keep cosigners in the same interview (https://docassemble.org/docs/special.html#session_local)
1. Experiment with how to save the data of the files. There was something in the chat at one point about using some method other than `persistant=True`. Explore `.slurp()` (though have to watch memory).