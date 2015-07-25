===
SSH
===

See `HLRS SSH Wiki <https://wickie.hlrs.de/platforms/index.php/Secure_Shell_ssh>`_.

First you need access to the hornet cluster. They also send you the password in a seperate email.

1. Install openssh.
2. Test if this works ``ssh username@hornet.hww.de``

To automatically authenticate, you need ssh keys.
Create ssh-keys and copy the public key to the hornet::

  $ ssh-keygen -t rsa -b 4096 -C "your.mail@mailprovider.domain" -t ~/.ssh/id_hornet4096_rsa
  $ scp ~/.ssh/id_hornet4096_rsa.pub username@hornet.hww.de:~/.ssh/id_hornet4096_rsa.pub
  $ ssh username@hornet.hww.de
  $ cat ~/publickeyfile >> authorized_keys2
  $ chmod 700 ~/.ssh

----------------
Github/Bitbucket
----------------

To clone a repository from github or bitbucket, you have to setup a ssh tunnel.
Choose two free ports for the hosts and login to the hornet::

  $ ssh -R42420:bitbucket.org:22 -R42421:github.com:22 hpcmscdz@hornet.hww.de

On the hornet you need ssh keys for github and bitbucket. Both websites need your public key::

  $ ssh-keygen -t rsa -b 4096 -C "username@hornet.hww.de" -t ~/.ssh/id_bitbucket4096_rsa
  $ ssh-keygen -t rsa -b 4096 -C "username@hornet.hww.de" -t ~/.ssh/id_github4096_rsa

Go to bitbucket/github and in your settings add the public keys. You have to fill in the contents of the ``id_bitbucket4096_rsa.pub`` and ``id_github4096_rsa.pub`` files.


Now you need a config file, which tells them that your host is actually ``127.0.0.1:port``::

  # ~/.ssh/config
  Host bitbucket.org
       IdentityFile ~/.ssh/id_bitbucket4096_rsa
       HostName 127.0.0.1
       Port 42420
  Host github.com
       IdentityFile ~/.ssh/id_github4096_rsa
       HostName 127.0.0.1
       Port 42421

Now you should be able to do::

  $ ssh -vT git@github.com
  $ git clone git@github.com:username/reponame.git

